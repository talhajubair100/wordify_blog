from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:post_id>', views.detail_post, name='detail-post'), 
    path('category/<ctg_name>', views.category_by_list, name='category-list'), 
    path('search', views.search_post, name='search')
]