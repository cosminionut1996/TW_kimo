from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from kimo.models import Device


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