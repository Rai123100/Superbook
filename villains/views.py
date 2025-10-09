# villains/views.py
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Villain
from .forms import VillainForm

class VillainListView(ListView):
    model = Villain
    template_name = "villains/lista_viloes.html"
    context_object_name = "viloes"
    ordering = ["codinome"]

class VillainDetailView(DetailView):
    model = Villain
    template_name = "villains/detalhe_vilao.html"
    context_object_name = "vilao"

class VillainCreateView(CreateView):
    model = Villain
    form_class = VillainForm
    template_name = "villains/form_vilao.html"
    success_url = reverse_lazy("lista_viloes")

class VillainUpdateView(UpdateView):
    model = Villain
    form_class = VillainForm
    template_name = "villains/form_vilao.html"
    success_url = reverse_lazy("lista_viloes")

class VillainDeleteView(DeleteView):
    model = Villain
    template_name = "villains/confirmar_exclusao.html"
    success_url = reverse_lazy("lista_viloes")



