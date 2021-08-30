from django.contrib.auth import get_user_model, get_user
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView

from .forms import CommentForm
from .models import BlogPost


class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser or self.request.user.is_staff:
            return queryset

        return queryset.filter(published=True)


def post_detail(request, slug):
    template_name = 'blog/blogpost_detail.html'
    post = get_object_or_404(BlogPost, slug=slug)
    comments = post.comments.filter()
    new_comment = None
    user = get_user(request)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = user
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
