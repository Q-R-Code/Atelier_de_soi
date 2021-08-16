from django.shortcuts import render



def home_blog(request):
    return render(request, 'blog/home_blog.html')
