from django.db import connection
from django.shortcuts import render
from django.views.generic import View

from django.contrib.auth import authenticate
from kimo.models import Copil
from kimo.models import Legatura


from kimo.models import Utilizator

import cx_Oracle


class Index(View):
    def get(self, request):
        return render(request, 'kimo/kimo.html')

    def post(self, request):
        return render(request, 'kimo/kimo.html')


class Login(View):
    def get(self, request):
        return render(request, 'kimo/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        r = authenticate(request, username=username, password=password)
        print(r, username)

        return render(request, 'kimo/login.html', context={
            'error': r
        })


class Register(View):
    def get(self, request):
        return render(request, 'kimo/register.html')

    def post(self, request):
        return render(request, 'kimo/register.html')


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

    def get(self, request):
        idp=10055
        l=list()
        for linie in Copil.objects.raw('SELECT * FROM Copil c JOIN LEGATURA l on l.id_copil=c.id where l.id_parinte={}'.format(idp)):
            l.append({'nume': linie.nume+' '+linie.prenume, 'locatie':linie.ultima_locatie})
            print(linie.nume, linie.prenume, linie.ultima_locatie)
        return render(request, 'kimo/profile.html', context={
            "result": l})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        r = authenticate(request, username=username, password=password)
        print(r, username)

        return render(request, 'kimo/profile.html', context={
            'error': r
        })