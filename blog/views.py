"""the main functions of the Blog app"""

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .forms import CommentForm
from .models import BlogPost


class BlogHome(ListView):
    """Return a list of article"""
    model = BlogPost
    context_object_name = "posts"

    def get_queryset(self):
        """If its a staff or admin user, return all the articles, else return just published articles"""
        queryset = super().get_queryset()
        if self.request.user.is_superuser or self.request.user.is_staff:
            return queryset

        return queryset.filter(published=True)


def post_detail(request, slug):
    """allows the display of an article. initialize the comment system"""
    template_name = 'blog/blogpost_detail.html'
    post = get_object_or_404(BlogPost, slug=slug)
    comments = post.comments.filter()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
