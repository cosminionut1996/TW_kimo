import matplotlib.path as mplPath
import numpy as np

import datetime
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from kimo.models import Device, Notificari, Signals
import json


from settings import SESSION_USER_ID_FIELD_NAME


class RequestPictureView(APIView):
    def post(self, request, format=None):
        poza = request.data.get('poza')
        if not poza:
            return Response("Required fields not completed", status=status.HTTP_400_BAD_REQUEST)


class CheckChildren(APIView):
    def get(self, request, format=None):
        res = Device.objects.raw(
            'select u.id as "id", c.prenume as "pren", d.latitudine as "lat", d.longitudine as "lon", r.coordinates as "crd" '
            'from utilizator u '
            'join legatura l on l.id_parinte=u.id '
            'join copil c on c.id=l.id_copil '
            'join device d on d.id_copil=c.id  '
            'join zona_risc r on u.id=r.id_utilizator')

        for x in res:
            bbPath = mplPath.Path(
                np.array([[d["lat"], d["lng"]]
                          for d in json.loads(x.crd.replace("'", '"'))])
            )
            if bbPath.contains_point((x.lat, x.lon)):
                Notificari(
                    titlu="Zona riscanta!",
                    continut="{} a intrat intr-o zona riscanta !".format(x.pren),
                    ora=datetime.datetime.now(),
                    culoare='red',
                    id_parinte=x.id).save()

        return Response("Done", status=status.HTTP_200_OK)


class LocationView(APIView):
    def put(self, request, token, format=None):
        longitudine = request.data.get('longitudine')
        latitudine = request.data.get('latitudine')
        if not longitudine or not latitudine:
            return Response("Required fields not completed", status=status.HTTP_400_BAD_REQUEST)
        try:
            Device.objects.filter(token=token).update(
                longitudine=longitudine,
                latitudine=latitudine
            )
        except:
            return Response("Token does not exist", status=status.HTTP_400_BAD_REQUEST)
        return Response("", status=status.HTTP_201_CREATED)


class SendSignal(APIView):
    def get(self, request, token, format=None):
        try:
            res = Device.objects.raw(
                'select s.text as "text", s.id as "sigid", d.id '
                'from signals s '
                'join copil c on c.id=s.id_copil '
                'join device d on d.id_copil=c.id  '
                'where d.token = \'{}\''.format(token))

            for x in res:
                txt = x.text
                sigid = x.sigid
                Signals.objects.filter(id=sigid).delete()
                return Response({"signal": txt}, status=status.HTTP_200_OK)

        except Exception as exc:
            return Response({"signal": "-"}, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response({"signal": "-"}, status=status.HTTP_206_PARTIAL_CONTENT)


class Cazaturi(APIView):
    def get(self, request, token, format=None):
        try:
            res = Device.objects.raw(
                'select u.id as "id", c.prenume as "pren" '
                'from utilizator u '
                'join legatura l on l.id_parinte=u.id '
                'join copil c on c.id=l.id_copil '
                'join device d on d.id_copil=c.id  '
                'where d.token = \'{}\''.format(token))

            for x in res:
                pren = x.pren
                uid = x.id
                print(uid, pren)

                Notificari.objects.create(
                    id_parinte=uid,
                    titlu="Accident!",
                    continut="{} s-a accidentat !".format(pren),
                    ora=datetime.datetime.now(),
                    culoare="orange",
                )
                break
        except Exception as exc:
            return Response({"response": str(exc)}, status=status.HTTP_200_OK)

        return Response({"response": "got it!"}, status=status.HTTP_200_OK)
