from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# student/4/


def search(request, name, classname):
    return HttpResponse('班级是：%s 学生：%s' % (classname, name))

# 匹配年月日 /student/time/2019!04!02


def check(request, year, month, day):
    return HttpResponse('year:%s,month:%s,day:%s' % (year, month, day))

# student/getuser?uname='jack'
def getuser(request): # 获取用户 uname
    getname = request.GET.get('uname')
    return HttpResponse('用户信息：%s' % getname)

def getre(request, year, month, day):
    return HttpResponse('匹配成功:%s' % year)

