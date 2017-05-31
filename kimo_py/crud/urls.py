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

app_name = 'crud'
urlpatterns = [
    url(r'^$', views.CRUD.as_view(), name='index'),
    url(r'^insert', views.CrudInsert.as_view(), name='insert'),
    url(r'^update', views.CrudUpdate.as_view(), name='update'),
    url(r'^delete', views.CrudDelete.as_view(), name='delete'),
    url(r'^read', views.CrudRead.as_view(), name='read'),
    url(r'^export', views.ExportTable.as_view(), name='export'),
    url(r'^children', views.CrudChildren.as_view(), name='num_children'),
]
