# villains/urls.py
from django.urls import path
from .views import lista_viloes

urlpatterns = [
    path('', lista_viloes, name='lista_viloes'),
]

