from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from .models import Pytanie


def index(request):
    lista_pytan = Pytanie.objects.order_by('-data_publikacji')
    template = loader.get_template('ankieta/index.html')
    context = {
        'lista_pytan': lista_pytan,
    }
    return HttpResponse(template.render(context, request))


def szczegoly(request, pytanie_id):
    return HttpResponse(f"<H1>Szczegóły</H1> {pytanie_id}")


def wyniki(request, pytanie_id):
    return HttpResponse(f"<H1>Wyniki</H1> {pytanie_id}")


def glosuj(request, pytanie_id):
    return HttpResponse(f"<H1>Głosuj</H1> {pytanie_id}")


    #permission_classes = [permissions.IsAuthenticated]
