"""mammoth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views

app_name = 'statistics'
urlpatterns = [
    url(r'^$', views.Stats.as_view(), name='index'),
    url(r'^obiecte', views.Obiecte.as_view(), name='obiecte'),
    url(r'^sol', views.Sol.as_view(), name='sol'),
    url(r'^animale', views.Animale.as_view(), name='animale'),
    url(r'^not', views.Not.as_view(), name='not'),


]
