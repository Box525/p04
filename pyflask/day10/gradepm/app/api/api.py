from flask_restful import Resource,abort,reqparse
from flask import render_template,jsonify
from app.models.admin.admin import Admin


# 要接收哪些参数
parse_get = reqparse.RequestParser()
parse_get.add_argument('admin')
parse_get.add_argument('pw')
parse_get.add_argument('rid')

# 404 abort

class UserApi(Resource):
    def get(self):
        #暂时作为 添加 admin 用户的入口
        args = parse_get.parse_args()
        print(args)
        admin = Admin(aid='12345678901',aname=args.admin,aemail='1234@163.com',apasswd=args.pw,rid=1)
        admin.save()
        return jsonify(admin=args.admin,pw=args.pw)
        # return render_template('main/index1.html')

from app.models.role.role import Role
class Limits(Resource):
    def get(self):
        args = parse_get.parse_args()
        rid = args.rid
        ls = Role.query.filter(Role.id == rid).first().limits
        print(ls)
        obj = {}
        data = []
        for item in ls:
            temp = {}
            temp['lname'] = item.rlname
            temp['lid'] = item.id
            data.append(temp)
        obj['data'] = data

        return jsonify(obj)

        
    

