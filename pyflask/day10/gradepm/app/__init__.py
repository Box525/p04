from flask import Flask

# 使用工厂模式来创建 flask app 对象
def create_app():
    #创建app对象
    app = Flask(__name__)
    #注册蓝图
    #ORM 模型 db的注册
    #如果有RESTful 也是需要在这注册

    return app
