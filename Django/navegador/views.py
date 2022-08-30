from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Olá mundo eu sou o navegador')


def norte(request):
    return render(request, 'navegador/norte.html')