from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView

def lista_post(request):
    posts = Post.objects.all()  # busca todos os heróis do banco
    return render(request, "posts/lista_posts.html", {"posts": posts})

def hello_posts(request):
    return HttpResponse("Bem-vindo ao módulo Posts!")

class PostListView(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"