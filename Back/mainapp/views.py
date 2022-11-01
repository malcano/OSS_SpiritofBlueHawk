from django.shortcuts import render
from .models import Post
def index(request):

    posts = Post.objects.all()

    return render(
        request,
        'mainapp/index.html',
        {
            'posts' : posts,
        }
    )
# Create your views here.
