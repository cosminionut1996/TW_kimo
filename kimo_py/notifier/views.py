from django.shortcuts import render
from django.views.generic import View


class Notifier(View):
    def get(self, request):
        return render(request, 'notifier/notifier.html')
