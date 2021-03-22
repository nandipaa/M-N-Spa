from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from .models import *
from django.core.mail import EmailMessage
from django.contrib.auth import settings
from .msg import send_sms, generateOTP
from django.views.generic import UpdateView

from django.contrib.auth import forms as auth_forms, views as auth_views
from django.contrib.auth import login as auth_login, authenticate as auth_authenticate


def index(request):
    return render(request, 'index.html', )


@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, ' Account was created for ' + username)

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
            messages.info(request, 'username or password is incorrect')
    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def sendSms(message, phone):
    send_sms('ACc575a7cb0fe8bfe7d0851c90e0cd8e56', 'f83d29d512a84d2e249cc93614ae6b0b', message, '+14076033805',
             phone)


code = generateOTP()


@login_required(login_url='login')
def booking(request):
    if request.method == 'POST':
        print(request.POST)

    book = BookingForm(request.POST)
    if book.is_valid():
        phone = book.cleaned_data['phone']
        book = book.save(commit=False)
        book.otp_code = code
        book.user = request.user
        book.save()
        messages.success(request, 'Form submission successful')

        message = f'''

         Hello {request.user.username}!

        Your Verification Code for M & N Spa is : {code}

        Make sure you give this code when attending booking

        Thank you for booking with us :)


                '''

        sendSms(message, phone)

        msg_body = f'''

        Hello {request.user.username}!

        Your Verification Code is for M & N Spa is  : {code}

        Make sure you give this code when attending booking

        Thank you for booking with us :)


        '''
        email = EmailMessage(
            'Booking verification code',
            msg_body,
            settings.EMAIL_HOST_USER,

            [request.POST.get('email')]
        )

        email.fail_silently = False
        email.send()

    context = {'book': book}

    return render(request, 'book.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def dashboard(request):
    bookings = Booking.objects.all()
    customer = Customer.objects.all()
    appointment = Appointment.objects.all()

    total_customers = customer.count()

    total_bookings = appointment.count()
    attended = appointment.filter(status='Attended').count()
    missed = appointment.filter(status='Missed').count()
    cancelled = appointment.filter(status='Cancelled').count()
    pending = appointment.filter(status='Pending').count()

    context = {'bookings': bookings, 'customer': customer,
               'total_customers': total_customers, 'total_bookings': total_bookings,
               'attended': attended, 'missed': missed, 'cancelled': cancelled,
               'pending': pending, 'appointment': appointment}
    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer', 'admin'])
def userPage(request):
    customer = Customer.objects.all()
    appointment = request.user.appointment_set.all()
    total_bookings = appointment.count()
    booking = Booking.objects.all()

    context = {'customer': customer, 'appointment': appointment, 'total_bookings': total_bookings, 'booking': booking}
    return render(request, 'userpage.html', context)


def packages(request):
    return render(request, 'packages.html')


def customer(request, pk):
    user = User.objects.get(id=pk)
    customer = Customer.objects.get(id=pk)
    appointment = user.appointment_set.all()
    appointment_count = appointment.count()
    context = {'customer': customer, 'appointment': appointment, 'appointment_count': appointment_count, 'user':user}
    return render(request, 'customer.html', context)


def verify(request):
    return render(request, 'verify.html')


def createCustomer(request):
    if request.method == 'POST':
        print(request.POST)
    custom = CustomerForm(request.POST)
    if custom.is_valid():
        custom.save()
        return redirect('dashboard')
    context = {'custom': custom}

    return render(request, 'create_customer.html', context)


def createBooking(request):
    if request.method == 'POST':
        print(request.POST)
    create = BookingForm(request.POST)
    if create.is_valid():
        create.save()
        return redirect('dashboard')

    context = {'create': create}
    return render(request, 'create_booking.html', context)


def updateBooking(request, pk):
    update = Booking.objects.get(id=pk)
    create = BookingForm(instance=update)

    if request.method == 'POST':
        create = BookingForm(request.POST, instance=update)
    if create.is_valid():
        create.save()
        return redirect('dashboard')

    context = {'create': create}

    return render(request, 'create_booking.html', context)


def deleteBooking(request, pk):
    update = Booking.objects.get(id=pk)

    if request.method == "POST":
        update.delete()
        return redirect('index')

    context = {'booking': update}
    return render(request, 'delete.html', context)


def updateCustomer(request, pk):
    update = Customer.objects.get(id=pk)
    custom = CustomerForm(instance=update)

    if request.method == 'POST':
        custom = CustomerForm(request.POST, instance=update)
    if custom.is_valid():
        custom.save()
        return redirect('dashboard')

    context = {'custom': custom}

    return render(request, 'create_customer.html', context)


def deleteCustomer(request, pk):
    update = Customer.objects.get(id=pk)

    if request.method == "POST":
        update.delete()
        return redirect('index')

    context = {'customer': update}
    return render(request, 'delete2.html', context)


def updateUser(request, id):
    update = Appointment.objects.get(id=id)
    appoint = AppointmentForm(instance=update)

    if request.method == 'POST':
        appoint = AppointmentForm(request.POST, instance=update)
    if appoint.is_valid():
        appoint = appoint.save(commit=False)
        appoint.user = request.user
        appoint.save(update_fields=['booking'])
        messages.success(request, 'Form update was successful')

        return redirect('index')

    context = {'appoint': appoint}

    return render(request, 'update_user.html', context)


@allowed_users(allowed_roles=['customer'])
def deleteUser(request, pk):
    update = Appointment.objects.get(id=pk)

    if request.method == "POST":
        update.delete()
        return redirect('userpage')

    context = {'booking': update}
    return render(request, 'delete_user.html', context)


