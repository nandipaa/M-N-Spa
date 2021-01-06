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
    path('verify', views.verify, name='verify'),
    path('createCustomer', views.createCustomer, name='create_customer'),
    path('createBooking', views.createBooking, name='create_booking'),
    path('updateBooking/<str:pk>/', views.updateBooking, name='update_booking'),
    path('deleteBooking/<str:pk>/', views.deleteBooking, name='delete_booking'),
    path('updateCustomer/<str:pk>/', views.updateCustomer, name='update_customer'),
    path('deleteCustomer/<str:pk>/', views.deleteCustomer, name='delete_customer'),
    path('userpage', views.userPage, name='userpage'),




]
