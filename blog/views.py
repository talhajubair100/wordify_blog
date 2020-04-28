from django.shortcuts import render
from .models import Category, Post, Profile

def search_post(request):
    if request.method == 'POST':
        search_keyword = request.POST['search_keyword']
        posts = Post.objects.filter(title__contains=search_keyword)
        return render(request, 'blog/search.html',{'posts': posts, 'search_key': search_keyword})
    
    return render(request, 'blog/search.html')


def detail_post(request, post_id):
    try:
        post_obj = Post.objects.get(id=post_id)
        #profile_obj = Profile.objects.get(user=post_obj.author)
        context = {'post': post_obj}
        return render(request, 'blog/detail_post.html', context)
    except:
        return render(request, '404.html')

def category_by_list(request, ctg_name):
    cteg_obj = Category.objects.get(name=ctg_name)
    post_list = Post.objects.filter(category=cteg_obj)
    context = {'posts': post_list, 'catg_name': ctg_name}
    return render(request, 'blog/post_by_category.html', context)