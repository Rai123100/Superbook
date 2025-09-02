from django.shortcuts import render
from django.http import HttpResponse
from .models import Hero
from django.views.generic import ListView

def lista_herois(request):
    herois = Hero.objects.all()  # busca todos os heróis do banco
    return render(request, "heroes/lista_herois.html", {"herois": herois})

def hello_heroes(request):
    return HttpResponse("Bem-vindo ao módulo Heroes!")

class HeroListView(ListView):
    model = Hero
    template_name = "heroes/lista_herois.html"
    context_object_name = "herois"