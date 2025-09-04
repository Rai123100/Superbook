from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView
from .forms import PostForm

def lista_post(request):
    posts = Post.objects.all()  # busca todos os heróis do banco
    return render(request, "posts/lista_posts.html", {"posts": posts})

def hello_posts(request):
    return HttpResponse("Bem-vindo ao módulo Posts!")

class PostListView(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"
    
    
# ----------------------------------------------------------------------Criar um post - com Modelform
def criar_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()

    return render(request, "posts/form_post.html", {"form": form})

