from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.urls import reverse

import random
import string


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
            return render(request, 'account_settings/token.html', context={
                'childname': firstname,
                'childlastname': lastname,
                'token': ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            })

        del request.session['child_firstname']
        del request.session['child_lastname']
        return HttpResponseRedirect(reverse('account_settings:child'))


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
