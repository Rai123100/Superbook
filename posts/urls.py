from django.urls import path
from .views import PostCreateView, PostListView, PostUpdateView, PostDeleteView, detalhe_post, toggle_pow

urlpatterns = [
    path('novo/', PostCreateView.as_view(), name='novo_post'),
    path('', PostListView.as_view(), name='lista_posts'),
    path('<int:pk>/editar/', PostUpdateView.as_view(), name='editar_post'),
    path('<int:pk>/excluir/', PostDeleteView.as_view(), name='excluir_post'),
    path('<int:pk>/', detalhe_post, name='detalhe_post'),
    path('<int:pk>/pow/', toggle_pow, name='toggle_pow'),  # NOVO
]
