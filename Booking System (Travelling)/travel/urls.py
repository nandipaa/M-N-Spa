from django.urls import path
from .import views


urlpatterns = [
    path('', views.index),
    path('packages', views.packages),
    path('contact', views.contact),
    path('book', views.book),
    path('login', views.login),
    path('dashboard', views.dashboard),




]