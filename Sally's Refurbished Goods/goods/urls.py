from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('clothes', views.clothes),
    path('household', views.household),
    path('eggs', views.eggs),
    path('about', views.about),
    path('services', views.services),
    path('contact', views.contact),

]