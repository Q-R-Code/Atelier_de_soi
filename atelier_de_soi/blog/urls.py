from django.urls import path

from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.BlogHome.as_view(), name='blog_home'),
    path('create/', views.BlogPostCreate.as_view(), name='create'),
    #path('<str:slug>/', views.BlogPostDetail.as_view(), name="post"),
    path('<slug:slug>/', views.post_detail, name='post')

]
