from flask import Flask
from app.extensions import db
import app.config as config


# 注册蓝图
def register_blueprint_with_app(app):
    from app.views.main import main as main_view
    app.register_blueprint(main_view)

# ORM注册
def register_mysql_with_app(app):
    db.init_app(app)

# 使用工厂模式来创建 flask app 对象
def create_app():
    #创建app对象
    app = Flask(__name__)
    app.debug = True
    app.config.from_object(config)
    #注册蓝图
    register_blueprint_with_app(app)
    #ORM 模型 db的注册
    register_mysql_with_app(app)
    #如果有RESTful 也是需要在这注册

    return app
