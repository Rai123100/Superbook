from django.db import models
from posts.models import Post

# Create your models here.

class Comentario(models.Model):
    texto = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    criado_em = models.DateTimeField(auto_now_add=True)
    