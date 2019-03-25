from flask import Flask
from app.extensions import db
import app.config as config
from flask_restful import Api
from app.api.api import UserApi as user_api
from app.api.api import Limits as limits_api

from flask import session
import os
from datetime import timedelta


# 注册蓝图
def register_blueprint_with_app(app):
    from app.views.main import main as main_view
    from app.views.user import user as user_view
    app.register_blueprint(main_view)
    app.register_blueprint(user_view)

# ORM注册
def register_mysql_with_app(app):
    db.init_app(app)

# 使用工厂模式来创建 flask app 对象
def create_app():
    #创建app对象
    app = Flask(__name__)
    app.debug = True
    app.config.from_object(config)
    #配置 session
    # app.config['SECRETKEY']
    app.secret_key = 'session_key'
    # 自定义设置 session的有效期
    # app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)
    # 配置 时间有效
    app.permanent_session_lifetime = timedelta(minutes=1)

    #注册蓝图
    register_blueprint_with_app(app)
    #ORM 模型 db的注册
    register_mysql_with_app(app)
    #如果有RESTful 也是需要在这注册
    api = Api(app)
    api.add_resource(user_api,'/userapi')
    api.add_resource(limits_api,'/api/v1/limits')

    return app
