from django.shortcuts import render
from django.views.generic import View


class Stats(View):
    def get(self, request):
        return render(request, 'statistics/index.html')

class Obiecte(View):
    def get(self, request):
        return render(request, 'statistics/obiecte.html')

class Sol(View):
    def get(self, request):
        return render(request, 'statistics/sol.html')

class Animale(View):
    def get(self, request):
        return render(request, 'statistics/animale.html')

class Not(View):
    def get(self,request):
        return render(request, 'statistics/not.html')