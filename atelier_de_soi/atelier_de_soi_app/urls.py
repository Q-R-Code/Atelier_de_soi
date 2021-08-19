"""atelier_de_soi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path(r'', views.index, name='home'),
    path(r'accueil/', include('main.urls', namespace='main')),
    path(r'blog/', include('blog.urls', namespace='blog')),
    path(r'compte/', include('account.urls', namespace='account')),
    path(r'admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path(r'__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
