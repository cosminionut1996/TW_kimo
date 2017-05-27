from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser


from peewee import DoesNotExist

from kimo.models import Utilizator


class MyAuthenticationBackend(object):
    def authenticate(self, request, username, password):
        try:
            utilizator = Utilizator.objects.get(username=username)
        except DoesNotExist:
            return None
        return utilizator.nume
