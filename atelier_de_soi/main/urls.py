from django.conf.urls import url
from django.urls import include

from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.index, name='home'),

]
