from django.shortcuts import render
from django.views.generic import View


class Map(View):

    def get(self, request):
        return render(request, 'live_map/google_map.html')
