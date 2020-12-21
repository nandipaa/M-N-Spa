from .import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('gauteng', views.gauteng),
    path('limpopo', views.limpopo),
    path('mpumalanga', views.mpumalanga),
    path('westerncape', views.westerncape),
    path('easterncape', views.easterncape),
    path('northerncape', views.northerncape),
    path('northwest', views.northwest),
    path('kwazulu', views.kwazulu),
    path('freestate', views.freestate),




]