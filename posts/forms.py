from django import forms
from .models import Post

# ---------------------- Com o Model - automatico
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['mensagem', 'autor']