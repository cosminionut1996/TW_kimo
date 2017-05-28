from django.contrib.sessions import models
from django.urls import reverse
from django.http import HttpResponseRedirect

from settings import SESSION_USER_ID_FIELD_NAME
from kimo import views

from kimo.models import Utilizator


class Authenticator(object):

    def __init__(self):
        self.session = models.Session()

    def authenticate(self, request, username, password):
        utilizator = Utilizator.objects.get(username=username)
        return utilizator.nume

    def get_user(self, user_id):
        utilizator = Utilizator.get(id=user_id)
        return utilizator


def logged_in_only(func):
    def wrap(self, request, *args, **kwargs):
        if request.session.get(SESSION_USER_ID_FIELD_NAME):
            return func(self, request, *args, **kwargs)
        return HttpResponseRedirect(reverse(viewname=views.Login))
    return wrap
