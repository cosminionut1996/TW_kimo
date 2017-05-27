from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


class Map(View):
    def get(self, request):
        return render(request, 'live_map/google_map.html')


class Danger(View):
    def get(self, request):
        return render(request, 'live_map/danger_area.html')
