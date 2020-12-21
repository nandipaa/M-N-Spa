from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import Booking, Contact


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('name', 'surname', 'email', 'confirm_email', 'number', 'packages', 'people', 'booking_date')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter Name'}),
            'surname': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter Name'}),
            'number': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter Cellphone Number'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Enter Email'}),
            'confirm_email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Enter Email'}),


        }


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'surname', 'email', 'message')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter Name'}),
            'surname': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter Name'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Enter Email'}),
            'message': forms.Textarea(attrs={'class': 'textarea', 'rows': 10, 'placeholder': ' write your message here '})


        }










