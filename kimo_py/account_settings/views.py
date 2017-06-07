from django.shortcuts import render
from django.views.generic import View

from django.http import HttpResponseRedirect
from django.urls import reverse

import random
import string

from kimo.models import Device, Copil


from kimo.models import Copil
from kimo.models import Legatura
from settings import SESSION_USER_ID_FIELD_NAME


class AccountSettings(View):
    def get(self, request):
        return render(request, 'kimo/base.html')


class Child(View):
    def get(self, request):
        return render(request, 'account_settings/child.html')

    def post(self, request):
        try:

            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            request.session['child_firstname'] = firstname
            request.session['child_lastname'] = lastname
            return HttpResponseRedirect(reverse('account_settings:token'))

            parinte=request.session.get(SESSION_USER_ID_FIELD_NAME)
            firstname=request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            copil1=Copil.objects.create(
                nume=request.POST.get('firstname'),
                prenume=request.POST.get('lastname')
            )
            copil1.save()

            copil=Copil.objects.raw('Select * from (select * from copil order by id desc) where rownum<2')
            print(copil[0].prenume,copil[0].id)

            legatura=Legatura.objects.raw('insert into legatura(id_parinte,id_copil) values ({},{})'.format(parinte,copil[0].id))


        except Exception as exc:
            e = exc
            return render(request, 'account_settings/child.html', context={
                'error': e
            })


class Token(View):
    def get(self, request):
        firstname = request.session.get('child_firstname')
        lastname = request.session.get('child_lastname')
        if firstname and lastname:
            del request.session['child_firstname']
            del request.session['child_lastname']
            token = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            Copil.objects.create(prenume=firstname, nume=lastname)
            c = Copil.objects.filter(prenume=firstname, nume=lastname)[0]
            Device.objects.create(id_copil=c.id, token=token)
            Legatura.objects.create(id_copil=c.id, id_parinte=request.session[SESSION_USER_ID_FIELD_NAME])

            return render(request, 'account_settings/token.html', context={
                'childname': firstname,
                'childlastname': lastname,
                'token': token
            })
        try:
            del request.session['child_firstname']
            del request.session['child_lastname']
        except:
            pass
        return HttpResponseRedirect(reverse('account_settings:add_child'))


class Pass(View):
    def get(self, request):
        return render(request, 'account_settings/change_password.html')

    def post(self,request):
        e='Success'
        try:
            new_password=request.POST.get('password')
            print(new_password)
        except Exception as exc:
            e = exc
        return render(request, 'account_settings/change_password.html', context={
            'error': e,
            })
