# 1.导入蓝图包
from flask import Blueprint
# 2.注册蓝图
# Blueprint()
main = Blueprint('main',__name__,url_prefix='/main/api/v1',template_folder='templates')
from . import views
# from ..models import student