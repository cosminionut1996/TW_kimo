from django import template
from settings import SESSION_USER_ID_FIELD_NAME

from kimo.models import Utilizator
import cx_Oracle

# Tags
register = template.Library()


def get_numar_copii(username):
    ip = '192.168.0.103'
    ip = '172.20.10.9'
    connection = cx_Oracle.connect('HR/hr@{}:1521/xe'.format(ip))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM num_questions WHERE username = '{}'".format(username))
    for x in cursor:
        return x[1]


@register.simple_tag(name='get_profile')
def get_profile(_id):
    utilizator = Utilizator.objects.get(id=int(_id))
    _dict = dict(
        numar_copii=get_numar_copii(utilizator.username),
        nume=utilizator.nume,
        prenume=utilizator.prenume,
        username=utilizator.username,
        email=utilizator.email,
        adresa=utilizator.adresa,
        localitate=utilizator.localitate
    )
    return _dict
