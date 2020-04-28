from blog.models import Category, Post


def mycontetxt(request):
    categories = Category.objects.all()
    latest_post = Post.objects.order_by('-date')[:3]
    return {'categories': categories, 'latest_post': latest_post}
