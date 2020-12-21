from django.urls import path
from .import views
from .views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('loginPage', views.loginPage, name='login'),
    path('register', views.register, name='register'),
    path('logoutUser', views.logoutUser, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('rooms', views.rooms, name='rooms'),
    path('reservation_list/', ReservationList.as_view(), name='ReservationList'),
    path('room_list/', RoomList.as_view(), name='RoomList'),
    path('reservation/', ReservationView.as_view(), name='ReservationView' )



]