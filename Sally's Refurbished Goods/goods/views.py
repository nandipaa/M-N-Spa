from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def clothes(request):
    return render(request, 'clothes.html')


def household(request):
    return render(request, 'household.html')


def eggs(request):
    return render(request, 'eggs.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')