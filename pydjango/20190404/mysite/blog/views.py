from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Country, Auther

# Create your views here.

def index(request):

    return render(request, 'blog/index.html')


def add_country(request):
    cname = request.POST.get('cname')

    # # 增
    # # 第一种写法插入数据表
    # new_country = Country.objects.create(cname=cname)
    # # 第二种方式插入数据表
    # new_country = Country(cname=cname)
    # new_country.save()

    # # 查
    # # all() = select * from 表名;
    # countrys = Country.objects.all()
    # # 只需要制定的列
    # countrys = Country.objects.all().only('cid','cname')
    # print(countrys)
    # for item in countrys:
    #     print(item.cid,':', item.cname)
    #
    # countrys = Country.objects.all().defer('cid')
    # for item in countrys:
    #     print(item.cid,':', item.cname)
    # # [start:count]
    # countrys = Country.objects.all()[:3]
    # # first()
    # # last()

    # 条件查
    # filter(条件)
    # country = Country.objects.filter(cid=1, cname='china').first()
    # print(country.cname)

    # update
    # Country.objects.filter(cid=1).update(cname='china123')

    # auther = Auther.objects.create(aname='jack', aaid='1001', cid_id=1)
    auther = Auther.objects.get(aid=1).cid.cname
    # # country = Country.objects.filter(cid=auther.cid)
    # print(auther)
    authers = Country.objects.get(cid=1).authers.all()
    # print(authers)

    return HttpResponse('hello world:%s' % cname)