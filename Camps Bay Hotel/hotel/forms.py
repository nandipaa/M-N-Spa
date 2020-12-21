from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Hollywood Twin Room', 'Hollywood Twin Room'),
        ('Cabana', 'Cabana'),
        ('Studio', 'Studio'),
        ('Suite', 'Suite'),

    ]

    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M"])
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M"])


