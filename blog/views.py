from django.shortcuts import get_object_or_404, render, redirect
from taggit.models import Tag
from .models import Category, Post, Comment
from .forms import *
#from django.template.defaultfilters import slugify


def create_post(request):
    forms = CreatePostForm()
    common_tags = Post.tags.most_common()[:4]

    if request.method == 'POST':
        forms = CreatePostForm(request.POST, request.FILES)
        if forms.is_valid():
            post_form = forms.save(commit=False)
            post_form.author = request.user
            post_form.save()
            forms.save_m2m()
            return redirect('/')
    context = {
        'forms': forms,
        'common_tags': common_tags

    }
    return render(request, "blog/create_post.html", context)

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Post.tags.most_common()[:4]
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'common_tags':common_tags,
        'posts':posts,
    }
    return render(request, 'blog/create_post.html', context)


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
        comments = post_obj.comments.all()
        form = CommentForm()
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment_form = form.save(commit=False)
                comment_form.post = post_obj
                comment_form.save()
                return redirect(post_obj)

        context = {
            'post': post_obj, 
            'comments': comments, 
            'form': form
            }
        return render(request, 'blog/detail_post.html', context)
    except:
        return render(request, '404.html')

def category_by_list(request, ctg_name):
    cteg_obj = Category.objects.get(name=ctg_name)
    post_list = Post.objects.filter(category=cteg_obj)
    context = {'posts': post_list, 'catg_name': ctg_name}
    return render(request, 'blog/post_by_category.html', context)

