from django.shortcuts import render
from django.views.generic import View
from kimo.authentication import logged_in_only
from settings import SESSION_USER_ID_FIELD_NAME


class Stats(View):
    @logged_in_only
    def get(self, request):
        idc = request.session.get(SESSION_USER_ID_FIELD_NAME)
        return render(request, 'statistics/index.html' ,context={'id':idc})


class Obiecte(View):
    @logged_in_only
    def get(self, request):
        idc = request.session.get(SESSION_USER_ID_FIELD_NAME)
        return render(request, 'statistics/obiecte.html',context={'id':idc})


class Sol(View):
    @logged_in_only
    def get(self, request):
        idc = request.session.get(SESSION_USER_ID_FIELD_NAME)
        return render(request, 'statistics/sol.html',context={'id':idc})


class Animale(View):
    @logged_in_only
    def get(self, request):
        idc = request.session.get(SESSION_USER_ID_FIELD_NAME)
        return render(request, 'statistics/animale.html',context={'id':idc})


class Not(View):
    @logged_in_only
    def get(self,request):
        return render(request, 'statistics/not.html')
