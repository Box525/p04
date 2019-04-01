from django.shortcuts import render
# 1.引入Django中的响应类
from django.http import HttpResponse

# Create your views here.


# 2.实现视图函数

# TODO:这是一个注释
def home(request):
    return HttpResponse('hello world!!!!')
