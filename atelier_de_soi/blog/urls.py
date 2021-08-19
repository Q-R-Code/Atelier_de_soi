from django.urls import path

from .views import BlogHome, BlogPostCreate, BlogPostDetail

app_name = 'blog'


urlpatterns = [
    path('', BlogHome.as_view(), name='blog_home'),
    path('create/', BlogPostCreate.as_view(), name='create'),
    path('<str:slug>/', BlogPostDetail.as_view(), name="post"),

]
