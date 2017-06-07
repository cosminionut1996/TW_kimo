from django.shortcuts import render
from django.views.generic import View
from kimo.authentication import logged_in_only
from settings import SESSION_USER_ID_FIELD_NAME
from kimo.models import ZonaRisc, Device

import json


class Map(View):
    @logged_in_only
    def get(self, request):
        return render(request, 'live_map/google_map.html', context={
            'zone': ZonaRisc.objects.filter(
                id_utilizator=request.session.get(SESSION_USER_ID_FIELD_NAME)
            ),
            'copii': Device.objects.raw('Select d.id, d.id_copil,d.longitudine,d.latitudine,c.nume,c.prenume from device d join copil c on d.id_copil=c.id join legatura l on l.id_copil= c.id join utilizator u on u.id=l.id_parinte where u.id={}'.format(request.session.get(SESSION_USER_ID_FIELD_NAME)) )
        })


class Danger(View):
    @logged_in_only
    def get(self, request):
        return render(request, 'live_map/danger_area.html')

    @logged_in_only
    def post(self, request):
        d = json.loads(request.POST.get('jsonText'))
        zone_name = d.get("name")
        zone_description = d.get("description")
        zone_coordinates = d.get("coordinates")
        id_utilizator = request.session.get(SESSION_USER_ID_FIELD_NAME)
        new_zone = ZonaRisc(name=zone_name,
                            description=zone_description,
                            coordinates=zone_coordinates,
                            id_utilizator=id_utilizator)
        new_zone.save()

        return render(request, 'live_map/danger_area.html')
