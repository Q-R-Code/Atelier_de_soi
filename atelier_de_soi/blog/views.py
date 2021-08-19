from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView

from .models import BlogPost


class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser or self.request.user.is_staff:
            return queryset

        return queryset.filter(published=True)


class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = 'blog/blogpost_create.html'
    fields = ['title', 'content', ]


class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"
