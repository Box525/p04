from flask_restful import reqparse,abort,Resource
# 引入json 格式化包 jsonify
from flask import jsonify
from app.models.student import Student as Stu


# abort 自定义信息提醒 当出现异常时 有时候正常情况、网络异常
# 4xx 和 5xx
def abort_if_error_info_doesnt_exist(info):
    if info is None:
        abort(404, message='扯犊子，404了!!!!')


parser_get = reqparse.RequestParser()
parser_get.add_argument('sname',type=str,required=True)

parser_post = reqparse.RequestParser()
parser_post.add_argument('sname', type=str, required=True)

#学生管理
#学生列表
#学生添加
#学生修改
#学生删除
class Student(Resource):
    # 获取学生的个人信息
    def get(self):
        # 操作数据库
        args = parser_get.parse_args()
        print(args)

        abort_if_error_info_doesnt_exist(info=None)
        return jsonify(msg='get',desc='这是restful HTTP动词GET方式')
    # 提交学生的个人信息:
    def post(self):
        args = parser_post.parse_args()
        print(args)
        return jsonify(msg='post',desc='这是restful HTTP动词POST方式')
    # 更新学生的个人信息:
    def put(self):
        return jsonify(msg='put', desc='这是restful HTTP动词PUT方式')
    # 删除学生
    def delete(self):
        return jsonify(msg='delete', desc='这是restful HTTP动词DELETE方式')

# 学生列表
# class Students(Resource):
