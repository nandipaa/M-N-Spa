from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('loginPage', views.loginPage, name='login'),
    path('register', views.register, name='register'),
    path('logoutUser', views.logoutUser, name='logout'),
    path('booking', views.booking, name='booking'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('packages', views.packages, name='packages'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('verify', views.verify, name='verify')

]
