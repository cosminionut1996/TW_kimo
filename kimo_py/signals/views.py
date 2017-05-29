from django.shortcuts import render
from django.views.generic import View
from kimo.authentication import logged_in_only


class Signal(View):
    @logged_in_only
    def get(self, request):
        return render(request, 'signals/index.html')
