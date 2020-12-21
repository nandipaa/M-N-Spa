from django.shortcuts import render
from .models import Booking, Contact
from .forms import ContactForm, BookingForm


def index(request):
    return render(request, 'index.html')


def packages(request):
    return render(request, 'packages.html')


def contact(request):

    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
             contact.save()

    contact = ContactForm()
    return render(request, 'contact.html', {'contact': contact})


def book(request):

    if request.method == 'POST':
        log = BookingForm(request.POST)
        if log.is_valid():
             log.save()

    log = BookingForm()
    return render(request, 'book.html', {'book': log})


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def dashboard(request):
    bookings = Booking.objects.all()
    contact = Contact.objects.all()
    return render(request, 'dashboard.html', {'bookings': bookings, 'contact': contact, })



