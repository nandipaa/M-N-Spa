from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from .models import *
from django.views.generic import ListView, FormView
from .forms import AvailabilityForm
from .availability import check_availability


def index(request):
    return render(request, 'index.html')


@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='guest')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

    else:
        messages.info(request, 'username OR password is incorrect')

        return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def dashboard(request):
    return render(request, 'dashboard.html')


def rooms(request):
    room = RoomCategory.objects.all()
    context = {'room': room}
    return render(request, 'rooms.html', context)


class ReservationList(ListView):
    model = Reservation


class RoomList(ListView):
    model = Room


class ReservationView(FormView):
    form_class = AvailabilityForm
    template_name = 'availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

                if len(available_rooms) > 0:
                    room = available_rooms[0]
                reservation = Reservation.objects.create(
                    check_in=data['check_in'],
                    check_out=data['check_out'],
                    guest=self.request.user,
                    room=room,
                )
                reservation.save()
                return HttpResponse(Reservation)
            else:
                return HttpResponse('This category of rooms are booked')
