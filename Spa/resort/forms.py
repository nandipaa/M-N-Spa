from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['phone', 'email', 'packages', 'people', 'booking_date']
        widgets = {'booking_date': forms.DateInput(attrs={'ID': 'datepicker'})}


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'surname', 'phone', 'email']


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['booking']



