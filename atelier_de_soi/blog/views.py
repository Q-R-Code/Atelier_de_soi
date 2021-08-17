from django.shortcuts import render
from django.views.generic import ListView

from .models import BlogPost


def home_blog(request):
    return render(request, 'blog/home_blog.html')


class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"