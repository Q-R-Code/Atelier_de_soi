from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path(r'', views.index, name='home'),
    path('<slug:slug>/', views.NewsPostDetail.as_view(), name='news'),
    path('mentions-legales', views.legal_notice, name='legal_notice'),

]
