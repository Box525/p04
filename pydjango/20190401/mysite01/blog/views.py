from django.shortcuts import render

# Create your views here.

# TODO:blog主页
def index(request):
    return render(request, 'blog/index.html')


def about(request):
    return render(request, 'about.html')


def blog_info(request):
    pass


def blog_login(request):
    pass


def blog_register(request):
    pass
