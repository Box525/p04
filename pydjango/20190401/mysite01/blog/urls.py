from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    path('about/<str:username>/', views.about, name='about'),
    url('login/', views.blog_login),
    url('add_auther/', views.blog_add_auther),
    url('check_pw', views.blog_check_pwd)
]

