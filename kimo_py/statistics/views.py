from django.shortcuts import render
from django.views.generic import View
from kimo.authentication import logged_in_only


class Stats(View):
    @logged_in_only
    def get(self, request):
        return render(request, 'statistics/index.html')


class Obiecte(View):
    @logged_in_only
    def get(self, request):
        return render(request, 'statistics/obiecte.html')


class Sol(View):
    @logged_in_only
    def get(self, request):
        return render(request, 'statistics/sol.html')


class Animale(View):
    @logged_in_only
    def get(self, request):
        return render(request, 'statistics/animale.html')


class Not(View):
    @logged_in_only
    def get(self,request):
        return render(request, 'statistics/not.html')
