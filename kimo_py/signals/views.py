from django.shortcuts import render
from django.views.generic import View
from kimo.authentication import logged_in_only
from kimo.models import ZonaRisc, Device, Copil, Signals
from settings import SESSION_USER_ID_FIELD_NAME


class Signal(View):
    @logged_in_only
    def get(self, request):
        return render(request, 'signals/index.html', context={
            'copii': Copil.objects.raw(
                'select c.id, c.nume, c.prenume from copil c join legatura l on l.id_copil=c.id join utilizator u on u.id=l.id_parinte where u.id ={}'.format(
                    request.session.get(SESSION_USER_ID_FIELD_NAME)))
        })

    @logged_in_only
    def post(self, request):
        id = request.POST.get('name')
        mesaj = request.POST.get('description')
        id_utilizator = request.session.get(SESSION_USER_ID_FIELD_NAME)
        print(id)
        sign = Signals(id_parinte=id_utilizator,
                            id_copil=id,
                            text=mesaj)
        sign.save()
        return render(request, 'signals/index.html')