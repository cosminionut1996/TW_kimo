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

app_name = 'kimo'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^login$', views.Login.as_view(), name='login'),
    url(r'^register$', views.Register.as_view(), name='register'),
    url(r'^profile', views.Profile.as_view(), name='profile'),
    url(r'^user_space/', views.UserSpace.as_view(), name='user_space'),
    # url(r'^injection_vulnerable/', views.InjectionVulnerable.as_view(), name='injection_vulnerable'),
    # url(r'^map/', views.Map.as_view(), name='map'),
    # url(r'^notification/', views.Notification.as_view(), name='notification'),
    # url(r'^add_child/', views.Child.as_view(), name='add_child'),
    # url(r'^admin/', admin.site.urls, name='admin'),
]
