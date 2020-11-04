from django.shortcuts import render
from blog.models import Post
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    posts = Post.objects.order_by('-date')
    context = {
                'posts': posts,
            }
    return render(request, 'home.html', context)

