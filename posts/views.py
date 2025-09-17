from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from comments.form import ComentarioForm
# ----------------------------------------------------------------------Baseado em função
# def lista_post(request): 
#     posts = Post.objects.all()  # busca todos os posts do banco
#     return render(request, "posts/lista_posts.html", {"posts": posts})

# def hello_posts(request):
#     return HttpResponse("Bem-vindo ao módulo Posts!")
    
# ----------------------------------------------------------------------Criar um post - com Modelform
# def criar_post(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('lista_posts')
#     else:
#         form = PostForm()

#     return render(request, "posts/form_post.html", {"form": form})

# ----------------------------------------------------------------------Criar um post - com GenericViews

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('lista_posts')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('lista_posts')
    
class PostListView(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/confirmar_exclusao.html'
    success_url = reverse_lazy('lista_posts')
    

def detalhe_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comentarios = post.comentarios.all()

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect('detalhe_post', pk=post.pk)
    else:
        form = ComentarioForm()

    return render(request, 'posts/detalhe_post.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form
    })
