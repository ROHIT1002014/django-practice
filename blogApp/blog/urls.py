from django.urls import path
from .views import homePageView, aboutPageView, blogDetail

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('blogs/', blogDetail, name='blogs'),
    path('blog-detail/<int:slug>/', blogDetail, name='blogDetail'),
]

