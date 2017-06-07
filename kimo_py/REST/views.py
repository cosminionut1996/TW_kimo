from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from kimo.models import Device

from django.http import HttpResponseRedirect

from settings import SESSION_USER_ID_FIELD_NAME


class RequestPictureView(APIView):
    def post(self, request, format=None):
        poza = request.data.get('poza')
        if not poza:
            return Response("Required fields not completed", status=status.HTTP_400_BAD_REQUEST)


class CheckChildren(APIView):
    def get(self, request, format=None):
        Device.objects.raw(
            'select u.id, d.latitudine, d.longitudine, r.coordinates from utilizator u join legatura l on l.id_parinte=u.id join copil c on c.id=l.id_copil join device d on d.id_copil=c.id  join zona_risc r on u.id= r.id_utilizator where u.id={}'.format(
                request.session.get(SESSION_USER_ID_FIELD_NAME)))

        return Response("Done", status=status.HTTP_400_BAD_REQUEST)



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

