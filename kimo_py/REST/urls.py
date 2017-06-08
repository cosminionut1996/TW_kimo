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

app_name = 'REST'
urlpatterns = [
    url(r'^token/(?P<token>[0-9A-Za-z]{6})$', views.LocationView.as_view(), name='location'),
    url(r'^signal/(?P<token>[0-9A-Za-z]{6})$', views.SendSignal.as_view(), name='signal'),
    url(r'^accident/(?P<token>[0-9A-Za-z]{6})$', views.Cazaturi.as_view(), name='accident'),
    url(r'^check$', views.CheckChildren.as_view(), name='check'),
]
