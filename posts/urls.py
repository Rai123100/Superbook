from django.urls import path
from . import views
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView, detalhe_post

urlpatterns = [
    # path('hello/', views.hello_posts, name='hello_post'),
    # path('lista/', views.lista_post, name='lista_posts'), Baseado em Função - def
    # path('novo/', criar_post, name='criar_post' ),
    path('lista/', PostListView.as_view(), name='lista_posts'),
    path('novo/', PostCreateView.as_view(), name='novo_post'),
    path('<int:pk>/editar/', PostUpdateView.as_view(), name='editar_post'),
    path('<int:pk>/excluir/', PostDeleteView.as_view(), name='excluir_post'),
    path('<int:pk>/detalhe', detalhe_post, name='detalhe_post'),
]