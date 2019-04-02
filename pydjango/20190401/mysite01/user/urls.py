from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # url(r'^$', views.home),#user/
    path('', views.home),# '' URL为空，表示当前是根路由
    url('index/', views.index),#user/index/
]
