from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('item','itemIndex','spotX','spotY','budget')