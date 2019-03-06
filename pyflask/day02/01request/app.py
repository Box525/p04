from flask import Flask, url_for, redirect, request, render_template
import json

app = Flask(__name__)


@app.route('/')
def index():
    return '这是一个index 主页'


# 获取指定班级的所有学生信息
@app.route('/class')
def get_students():
    print(request.url)  #http://127.0.0.1:5000/class?classname=py04
    #   request 请求中 flask 对于请求参数处理
    #   有3种方式：1.在URL中 ?classname=py04 参数列表
    # 2. 传统方式  form 表单的方式  key value
    # 3. json
    #对于URL中的请求处理
    print(request.args
          )  #ImmutableMultiDict([('classname', 'py04'), ('name', 'tom')])
    #取参数列表中的变量的值
    print(request.args['classname'])
    print(request.args.get('name'))
    print(list(request.args.keys()))
    print(list(request.args.values()))
    print(dict(request.args))
    # request.path 路由路径
    # request.full_path 全路径
    # request.method 获取请求的方法
    # request.host 获取主机地址
    # request.host_url
    # return '请求成功:%s' % (request.url)
    jsonobj = {'name': request.args.get('name'), 'age': 18, 'nickname': '王校长'}

    jsonString = json.dumps(jsonobj, ensure_ascii=False)

    return jsonString


@app.route('/user/')
def user():
    html_content = '''
   <form action="/user/login" method="POST" enctype="multipart/form-data">
    <input type="text" name="uname">
    <br />
    <input type="text" name="upasswd">
    <br />
    <input type="file" name="myfile">
    <br />
    <input type="submit" value="登录">
   </form>
   '''
    return html_content

@app.route('/user/login',methods=['POST'])
def login():
    print(request.args)
    print(request.form)
    file_obj = request.files['myfile']
    file_obj.save('./2.png')
    return '登录成功'


def isTrueOrFalse():
    res = True if 2 > 3 else False
    return res

@app.route('/jinjia')
def jinjia():
    user = ['a1','a2','a3']
    return render_template('index.html', title='这是传值',show=4,user=user)

@app.route('/home/')
def home():
    return render_template('about.html',head=True)

def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
