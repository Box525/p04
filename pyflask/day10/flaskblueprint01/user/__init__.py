# 1.导入蓝图包
from flask import Blueprint
# 2.注册蓝图
# Blueprint()
user = Blueprint('user',__name__,url_prefix='/user',template_folder='templates')
from . import views