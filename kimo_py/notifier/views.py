from django.shortcuts import render
from django.views.generic import View
from settings import SESSION_USER_ID_FIELD_NAME

from kimo.models import Notificari
from kimo.authentication import logged_in_only
from django.http import HttpResponseRedirect
from django.urls import reverse


class Notifier(View):

    @logged_in_only
    def get(self, request):
        id=request.session.get(SESSION_USER_ID_FIELD_NAME)
        notificare=Notificari.objects.filter(id_parinte=id)
        l=list()
        for linie in notificare:
            l.append({'titlu': linie.titlu,
                      'continut': linie.continut,
                      'culoare':linie.culoare})

        return render(request, 'notifier/notifier.html', context={
            "result": l
        })


class NotClear(View):

    @logged_in_only
    def get(self, request):
        id=request.session.get(SESSION_USER_ID_FIELD_NAME)
        Notificari.objects.filter(id_parinte=id).delete()
        return HttpResponseRedirect(reverse("notifier:notification"))
