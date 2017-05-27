from django.db import connection
from django.shortcuts import render
from django.views.generic import View

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
        return render(request, 'kimo/login.html')


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
        return render(request, 'kimo/profile.html')

    def post(self, request):
        return render(request, 'kimo/profile.html')
