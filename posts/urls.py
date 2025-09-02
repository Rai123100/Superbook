from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    path('hello/', views.hello_posts, name='hello_post'),
    path('lista/', views.lista_post, name='lista_posts'),
    path('cbv-lista/', PostListView.as_view(), name='cbv_lista_post'),
]