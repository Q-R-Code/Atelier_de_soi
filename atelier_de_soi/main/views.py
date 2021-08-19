from django.shortcuts import render

def index(request):
    return render(request, 'main/home.html')

def legal_notice(request):
    return render(request, 'main/legal_notice.html')