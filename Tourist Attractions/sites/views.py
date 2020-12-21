from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def gauteng(request):
    return render(request, 'gauteng.html')


def limpopo(request):
    return render(request, 'limpopo.html')


def mpumalanga(request):
    return render(request, 'mpumalanga.html')


def westerncape(request):
    return render(request, 'westerncape.html')


def easterncape(request):
    return render(request, 'easterncape.html')


def northerncape(request):
    return render(request, 'northerncape.html')


def northwest(request):
    return render(request, 'northwest.html')


def kwazulu(request):
    return render(request, 'kwazulu.html')


def freestate(request):
    return render(request, 'freestate.html')


