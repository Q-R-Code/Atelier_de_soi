from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import NewsPost


def index(request):
    news = NewsPost.objects.all().order_by('-created_on')
    for new in news :
        print(new.title)
    return render(request, 'main/home.html', {"news":news})


def legal_notice(request):
    return render(request, 'main/legal_notice.html')



class NewsPostDetail(DetailView):
    model = NewsPost
    template_name = 'news/newspost_detail.html'
    context_object_name = "news"
