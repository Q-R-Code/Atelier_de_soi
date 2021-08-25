from django.urls import path

from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.BlogHome.as_view(), name='blog_home'),
    path('<slug:slug>/', views.post_detail, name='post')

]
