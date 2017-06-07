from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View

from kimo.models import Utilizator, Copil
from kimo.authentication import logged_in_only
from settings import SESSION_USER_ID_FIELD_NAME

import datetime
import cx_Oracle


class Index(View):
    def get(self, request):
        return render(request, 'kimo/kimo.html')

    def post(self, request):
        return render(request, 'kimo/kimo.html')


class Login(View):
    def get(self, request):
        if request.session.get(SESSION_USER_ID_FIELD_NAME):
            del request.session[SESSION_USER_ID_FIELD_NAME]
        return render(request, 'kimo/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        utilizator = Utilizator.authenticate(username, password)
        if utilizator:
            utilizator.login(request)
            return HttpResponseRedirect(reverse('kimo:profile'))
        else:
            return render(request, 'kimo/login.html', context={
                "error": "Invalid username / password."
            })


class Register(View):
    def get(self, request):
        if request.session.get(SESSION_USER_ID_FIELD_NAME):
            del request.session[SESSION_USER_ID_FIELD_NAME]
        return render(request, 'kimo/register.html')

    def post(self, request):
        e = 'V-ati inregistrat cu success!'
        parola = request.POST.get('password')
        conf = request.POST.get('confirm-password')
        if parola not in [None, ''] and parola != conf:
            return render(request, 'kimo/register.html', context={
                'error': "The passwords do not match!",
            })

        try:
            Utilizator.objects.create(
                nume=request.POST.get('nume'),
                prenume=request.POST.get('prenume'),
                subscriptie='FREE',
                adresa=request.POST.get('adresa'),
                email=request.POST.get('email'),
                telefon=request.POST.get('telefon'),
                username=request.POST.get('username'),
                parola=parola,
                expirare=datetime.datetime.now() + datetime.timedelta(days=361),
                localitate=request.POST.get('localitate'),
                id=Utilizator.objects.all().count() + 1,
            )
        except Exception as exc:
            e = exc
            return render(request, 'kimo/register.html', context={
                'error': e,
            })
        else:
            return HttpResponseRedirect(reverse('kimo:profile'))


class InjectionVulnerable(View):

    def __init__(self):
        super().__init__()
        self.connection = cx_Oracle.connect('student/STUDENT@localhost:1521/xe')
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def get(self, request):
        return render(request, 'kimo/injection_vulnerable.html')

    def post(self, request):
        self.cursor.execute("SELECT * FROM USERS WHERE nume = '%s'" %
                            request.POST.get('nume'))
        error = ''.join([x for x in self.cursor])
        return render(request, 'kimo/injection_vulnerable.html', context={
            'error': error
        })


class UserSpace(View):

    def get(self, request):
        return render(request, 'kimo/user_space.html')

    def post(self, request):
        cursor = connection.cursor()
        try:
            ret = cursor.callfunc(
                'UTILIZATOR_FUNC.LOGIN',
                cx_Oracle.NUMBER,
                (request.POST.get('username'), request.POST.get('password'))
            )
        except Exception as exc:
            return render(request, 'kimo/user_space.html', context={
                "error": exc
            })

        return render(request, 'kimo/user_space.html', context={
            "error": int(ret)
        })


class Profile(View):

    @logged_in_only
    def get(self, request):
        idc = request.session.get(SESSION_USER_ID_FIELD_NAME)
        l = list()
        nr = 0
        for linie in Copil.objects.raw(
                'SELECT * '
                'FROM Copil c JOIN LEGATURA l on l.id_copil=c.id join utilizator p on p.id=l.id_parinte '
                'where l.id_parinte={}'.format(idc)
        ):
            l.append({'nume': linie.nume + ' ' + linie.prenume,
                      'locatie': linie.ultima_locatie})
            nr += 1

        linie = Utilizator.objects.get(id=idc)
        n_l = {
            'id': idc,
            'nume': linie.nume + ' ' + linie.prenume,
            'email': linie.email,
            'adresa': linie.adresa + ' / ' + linie.localitate
        }
        return render(request, 'kimo/profile.html', context={
            "result": l,
            "parinte": n_l,
            "numar": nr
        })

    @logged_in_only
    def post(self, request):
        return render(request, 'kimo/profile.html')

