from django.shortcuts import render

# Create your views here.

# TODO:blog主页
def index(request):
    # u_name = request.GET.get('uname')
    # u_pwd = request.GET.get('upwd')
    # u_name = request.POST.get('uname')
    # u_pwd = request.POST.get('upwd')
    data = {
        'info': {
            'u_name': '',
            'u_pwd': ''
        }
    }
    return render(request, 'blog/index.html', data)


def about(request, username):
    name = request.POST.get('uname')
    pwd = request.POST.get('upwd')
    print(name, pwd)
    return render(request, 'about.html')


def blog_info(request):
    pass

# TODO:用户登录
def blog_login(request):
    return render(request, 'login.html')


def blog_register(request):
    pass


from blog import models
def blog_add_auther(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        sex = request.POST.get('usex')
        # 将数据保存到数据库
        models.Auther.objects.create(aname=name, asex=sex)

    authers = models.Auther.objects.all()
    print(authers)
    return render(request, 'authers.html')


from django.shortcuts import redirect, reverse

def blog_check_pwd(request):
    #访问数据库判断用户是否 存在
    # return redirect(reverse('home'))
    name = request.POST.get('uname')

    return redirect(reverse('about', args=[name]))


def rootindex(request):
    return render(request, 'index.html')





