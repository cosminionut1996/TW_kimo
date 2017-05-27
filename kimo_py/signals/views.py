from django.shortcuts import render
from django.views.generic import View


class Signal(View):
    def get(self, request):
        return render(request, 'signals/index.html')
