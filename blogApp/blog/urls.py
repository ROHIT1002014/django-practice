from django.urls import path
from .views import (
    homePageView,
    aboutPageView,
    blog_detail_view,
    blog_list_view,
    blog_create_view,
    blog_update_view,
    blog_delete_view,
    )

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('blog/<str:slug>/', blog_detail_view, name='blogDetail'),
    path('blog-list/', blog_list_view, name='blogList'),
    path('blog-new/', blog_create_view, name='createBlog'),
    path('blog/<str:slug>/delete', blog_delete_view, name='deleteBlog'),
    path('blog/<str:slug>/edit', blog_update_view, name='updateBlog'),
]

