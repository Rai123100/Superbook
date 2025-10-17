from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_heroes, name='hello_heroes'),
    path('lista/', views.lista_herois, name='lista_herois'),
    # path('cbv-lista/', HeroListView.as_view(), name='lista_herois'),
    path('contato/', views.contato_view, name='contato'),
    path('novo/', views.criar_heroi, name='criar_heroi'),
    path('<int:pk>/editar/', views.editar_heroi, name='editar_heroi'),  
]