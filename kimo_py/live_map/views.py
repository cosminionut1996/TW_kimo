from django.shortcuts import render
from django.views.generic import View
from kimo.authentication import logged_in_only

from kimo.models import ZonaRisc

import json


class Map(View):
    @logged_in_only
    def get(self, request):
        zones = ZonaRisc.objects.filter()
        for zone in zones:
            print(zone.name, zone.description, zone.coordinates)
        return render(request, 'live_map/google_map.html')


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
        new_zone = ZonaRisc(name=zone_name,
                            description=zone_description,
                            coordinates=zone_coordinates)
        new_zone.save()
        return render(request, 'live_map/danger_area.html')
