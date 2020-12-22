from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only, booked_users
from django.contrib.auth.models import Group
from .models import *
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


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
            messages.success(request, ' Account was created for ' + username)
            group = Group.objects.get(name='customer')
            user.groups.add(group)

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


@login_required(login_url='login')
def booking(request):

    if request.method == 'POST':
        print(request.POST)
    book = BookingForm(request.POST)
    if book.is_valid():
        book.save()

    context = {'book': book}
    return render(request, 'book.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def dashboard(request):
    bookings = Booking.objects.all()
    customer = Customer.objects.all()
    system = System.objects.all()

    total_customers = customer.count()

    total_bookings = system.count()
    attended = system.filter(status='Attended').count()
    missed = system.filter(status='Missed').count()
    cancelled = system.filter(status='Cancelled').count()
    pending = system.filter(status='Pending').count()

    context = {'bookings': bookings, 'customer': customer,
               'total_customers': total_customers, 'total_bookings': total_bookings,
               'attended': attended, 'missed': missed, 'cancelled': cancelled,
               'pending': pending, 'system': system}
    return render(request, 'dashboard.html', context)


def packages(request):
    return render(request, 'packages.html')


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    systems = customer.system_set.all()
    systems_count = systems.count()
    context = {'customer': customer, 'systems': systems, 'systems_count': systems_count}
    return render(request, 'customer.html', context)


def verify(request):
    return render(request, 'verify.html')


def email(request):
    template = render_to_string('email.html', {'name' : request.user})
    email = EmailMessage(
        'You have successfully created your account! ',
        template,
        settings.EMAIL_HOST_USER,
        [request.user.email],
    )
    email.fail_silently = False
    email.send()

    return render(request, 'email.html')


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



