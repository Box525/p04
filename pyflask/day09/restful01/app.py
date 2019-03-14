from flask import Flask
from flask_restful import Api,abort,reqparse,Resource
import json
app = Flask(__name__)


@app.route('/',methods=['GET'])
def index():
    return '这是原始的URL 请求和响应方式'

########以上是flask 默认的 route 处理方式#########
####以下是 RESTful的处理方式
# 1. 初始化 RESTful  api对象 用于管理api接口
api = Api(app)

# 2. 处理参数（可选）
parser = reqparse.RequestParser()


# 3. 实现资源对象
class User(Resource):
    def get(self):
        # return json.dumps({'msg':'这是RESTful 的方式'},ensure_ascii=False)
        return {'msg':'这是RESTful 的方式'}
    def post(self):
        return {'msg':'post'}
# 4.设置路由
api.add_resource(User,'/user')


if __name__ == '__main__':
    app.run(debug=True)
    