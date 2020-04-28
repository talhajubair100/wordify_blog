from django.shortcuts import render
from blog.models import Post, Category

def home(request):
    posts = Post.objects.all()
    context = {
                'posts': posts,
            }
    return render(request, 'home.html', context)

