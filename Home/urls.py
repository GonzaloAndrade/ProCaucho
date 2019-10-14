#coding: utf8
from django.conf.urls import url
from django.views.generic import RedirectView

from Home import views

app_name = 'entries'
urlpatterns = [
    url(r'^$', views.home, name='index'),
]
