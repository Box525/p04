"""mysite01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # 导入Admin功能模块 后台管理
from django.urls import path, include, re_path # 导入URL编写模块
# TODO：3 注册路由
# import user.views as uv

# from user.views import UserView

# TODO：urlpatterns 用来设置整个URL集合，每一个元素代表一条URL信息
'''
path(URL的规则,指定的视图函数的名称,url的别名)
'''

import stu.views as sv
import blog.views as bv


urlpatterns = [
    path('student/<int:classname>/<str:name>', sv.search),
    path('student/time/<year>/<int:month>/<slug:day>/', sv.check),
    path('student/info', sv.getuser),
    path('', bv.rootindex),
    path('admin/', admin.site.urls),
    # path('user/', uv.home)
    # path('user/', UserView.as_view())
    path('user/', include(('user.urls', 'user'), namespace='user')),
    re_path(r'student/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/', sv.getre),
    # 开发模式
    path('blog/', include('blog.urls'))
]
