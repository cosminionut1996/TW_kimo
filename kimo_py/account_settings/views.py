from django.shortcuts import render
from django.views.generic import View


class AccountSettings(View):
    def get(self, request):
        return render(request, 'kimo/base.html')


class Child(View):
    def get(self, request):
        return render(request, 'account_settings/child.html')
    def post(selfself,request):
        e='Success'
        try:
            firstname=request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            print(firstname,lastname)
        except Exception as exc:
            e=exc
        return render(request, 'account_settings/child.html', context={
            'error':e
        })


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
