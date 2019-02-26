# 导入flask  包
from flask import Flask,url_for,redirect
# 创建一个 Flask的 Web应用 对象
# Flask程序都需要创建一个实例
# Web 服务器会使用WSGI协议，它会将接受到的客户端请求转交给
# 这个对象处理，此时此地可以理解为app 这个对象
# Flask 一般情况下需要一个参数 这个参数通常是主模块或者包的名称，
# 一般情况下使用 __name__ 作为参数
app = Flask(__name__)

# 定义路由视图 可以理解为 URL
@app.route('/')
# 使用app.route 装饰器 将 URL和执行的视图函数 的关系
# 进行关联，并将其保存在 app.url_map
@app.route('/home/')
# 以下函数 学名 在Flask中称之为视图函数
# 当访问 装饰器的时候也就是对应的URL 就会调用这个函数
# 当遇到第一个有效return 时就是 结束
# 其中的return 就是代表 response 响应
def index():
    return "这是一个Flask Web应用"

@app.route('/favicon.ico')
def favicon():
    return ''


def about2():
    return "<h1>这是一个关于的界面</h1>"

# flask中的路由另外一种方式，注意：需要使用view_func属性
app.add_url_rule('/about/',view_func=about2)

# 动态路由
@app.route('/class/<name>/<int:age>/')
def className(name,age):
    return '<h1>选中的班级是:' + name + '</h1>'

# 指定 请求动词
@app.route('/login/', methods=['get','post'])
def login():
    return '登录成功'

# 反向生成url 需要使用 flask  url_for 引出

@app.route('/reg/')
def register():
    print(url_for('login'))
    return redirect(url_for('login'),code=302)

if __name__ == '__main__':
    # 用来运行flask应用
    # 使用run()来启动 服务器
    app.run(port=8080,debug=True)
    