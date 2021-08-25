from django.shortcuts import render
from django.views.generic import DetailView

from .models import NewsPost


def index(request):
    """ return the home page with the news"""
    news_all = NewsPost.objects.filter(published=True)
    news = news_all.order_by('-id')[:3]
    return render(request, 'main/home.html', {"news": news})


def legal_notice(request):
    return render(request, 'main/legal_notice.html')


class NewsPostDetail(DetailView):
    """ this method return the detail of a news"""
    model = NewsPost
    template_name = 'news/newspost_detail.html'
    context_object_name = "news"
