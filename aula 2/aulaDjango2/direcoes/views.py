from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'direcoes/index.html')


def norte(request):
    return render(request, 'direcoes/norte.html')


def sul(request):
    return render(request, 'direcoes/sul.html')


def leste(request):
    return render(request, 'direcoes/oeste.html')


def oeste(request):
    return render(request, 'direcoes/leste.html')