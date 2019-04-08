from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/$', views.reg_view),
    url(r'^login/$', views.login),
    url(r'^register/check/$', views.register),
    url(r'search/', views.search)
]