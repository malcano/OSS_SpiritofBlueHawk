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

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'mainapp/single_post_page.html',
        {
            'post' : post,
        }
    )
