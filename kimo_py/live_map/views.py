from django.shortcuts import render
from django.views.generic import View
from kimo.authentication import logged_in_only


class Map(View):
    @logged_in_only
    def get(self, request):
        return render(request, 'live_map/google_map.html')


class Danger(View):
    @logged_in_only
    def get(self, request):
        return render(request, 'live_map/danger_area.html')
