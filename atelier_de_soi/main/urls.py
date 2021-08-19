from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path(r'', views.index, name='home'),
    path('mentions-legales', views.legal_notice, name='legal_notice'),

]
