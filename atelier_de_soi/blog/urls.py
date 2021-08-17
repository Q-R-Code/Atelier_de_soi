from django.conf.urls import url
from . import views
from .views import BlogHome

app_name = 'blog'


urlpatterns = [
    url('', BlogHome.as_view(), name='blog_home'),

]
