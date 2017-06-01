from django import template

from kimo.models import Utilizator

from settings import SESSION_USER_ID_FIELD_NAME

# Tags
register = template.Library()


@register.simple_tag
def get_num_jobs(request):
    if request.session.get(SESSION_USER_ID_FIELD_NAME):
        pass