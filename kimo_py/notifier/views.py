from django.shortcuts import render
from django.views.generic import View

from kimo.models import Notificari


class Notifier(View):
    def get(self, request):
        notificare=Notificari.objects.filter(id_parinte='10055')
        l=list()
        for linie in notificare:
            l.append({'titlu': linie.titlu, 'continut': linie.continut, 'culoare':linie.culoare})
        return render(request, 'notifier/notifier.html', context={
        "result": l
        })
