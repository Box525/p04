from django.shortcuts import render
# 1.引入Django中的响应类
from django.http import HttpResponse

# Create your views here.


# 2.实现视图函数

# TODO:这是一个注释
def home(request):
    return HttpResponse('hello world!!!!')


def index(request):
    return HttpResponse('这是首页')

# 第二种方式创建 视图对应
# Class-base views
# from django.views.generic.base import TemplateView
# #
# #
# class UserView(TemplateView):
#
#     def get(self, request):
#         return HttpResponse('Get')
#
#     def put(self, request):
#         return HttpResponse('Post')






