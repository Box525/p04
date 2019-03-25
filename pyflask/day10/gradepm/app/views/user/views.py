from . import user
from flask import render_template,redirect,url_for,request,jsonify,Response
from app.models.admin.admin import Admin
from app.models.gleader.gleader import GLeader
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature,SignatureExpired
import os
import time

# os.environ['TOKEN'] = ''


@user.route('/')
def index():
    # 加密 加盐哈希 MD5 Base64
    # 加盐 token 号令牌 专门用于信息验证
    # itsdangerous

    # 盐值
    '''
    salt = 'salt'
    ser = Serializer(salt,expires_in=20)
    token = ser.dumps({
        'user':'admin',
        'pw':'admin',
        'time':''
    })
    print(token)
    token_code = token.decode()
    print(token_code)
    os.environ['TOKEN'] = token_code
    '''

    # res = ser.loads(token_code)
    # print(res)

    return render_template('user/login.html')

@user.route('/ser')
def ser():
    salt = 'salt'
    ser = Serializer(salt,expires_in=20)
    try:
        # print(os.environ['TOKEN'])
        res = ser.loads(os.environ['TOKEN'])
        print(res)
        return 'ssssss'#jsonify(res)
    except Exception as e:
        raise e

    return '验证'

def set_serializer(msg):
    salt = 'salt'
    ser = Serializer(salt,expires_in=600)
    return ser.dumps(msg).decode()

def get_serializer(msg):
    pass

@user.route('/login',endpoint='login',methods=['POST'])
def login():
    args = request.form
    print(args)
    # 数据库的验证
    if args.get('username'):
        admin = Admin.query.filter(Admin.aname == args.get('username')).first()
        if admin:
            res = admin.verifyPW(args.get('password'))
            if res:
                # 登录成功 添加token （更新token）
                token = set_serializer({
                    'uname':args.get('username'),
                    'ltime':time.time()
                })
                resp = Response(render_template('main/index1.html'))
                # 设置cookie
                resp.set_cookie('token',token)
                return resp
                # return render_template('main/index1.html')
            else:
                # 密码错误
                # return redirect(url_for('user.index',msg='密码错误'))
                return render_template('user/login.html',pw_error=True)

        else:
            return '用户不存在'
    else:
        return '用户名必填'

    return render_template('main/index1.html')


@user.route('/userinfo',endpoint='user_info')
def userInfo():
    # 1.验证Token

    return render_template('main/index1.html',userinfo=True)

@user.route('/adduser',endpoint='add_user',methods=['POST'])
def addUser():
    #0.验证Token
    #1.查数据库
    args = request.form
    gleader = GLeader.query.filter(GLeader.lphone == args.get('lphone')).first()
    if gleader is None:
        #2.插入数据库
        sex = 0
        if args.get('lsex') == '男':
            sex=1

        new_gleader = GLeader(
            lphone=args.get('lphone'),
            lname=args.get('lname'),
            lemail=args.get('lemail'),
            lsex=sex)
        new_gleader.save()
    else:
        return '用户已存在'

    #3.返回 目的页
    return render_template('main/index1.html', userinfo=True)
