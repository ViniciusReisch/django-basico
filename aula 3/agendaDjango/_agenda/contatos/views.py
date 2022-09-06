from django.shortcuts import render
from .models import Contato


# Create your views here.
def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html',
                  {'contatos': contatos})


def amigos(request):
    contatos = Contato.objects.all().filter(categoria='3')
    return render(request, 'contatos/index.html',
                  {'contatos': contatos})

def familia(request):
    contatos = Contato.objects.all().filter(categoria='1')
    return render(request, 'contatos/index.html',
                  {'contatos': contatos})


def empresa(request):
    contatos = Contato.objects.all().filter(categoria='2')
    return render(request, 'contatos/index.html',
                  {'contatos': contatos})