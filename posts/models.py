from django.db import models
from heroes.models import Hero

# Create your models here.

class Post(models.Model):
    autor = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="posts")
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor.codinome}: {self.mensagem[:30]}..."

# Tabela de Curtida - Curtida = Pow

class Like(models.Model):
    heroi = models.ForeignKey(Hero, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('heroi', 'post') # uma regrinha para que não dê para curtir 2x

    def __str__(self):
        return f"{self.heroi.codinome} curtiu {self.post.id}"

