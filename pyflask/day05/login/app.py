from flask import Flask,render_template,url_for,redirect,request
import pymysql

app = Flask(__name__)

@app.route('/',endpoint='home')
@app.route('/login/',endpoint='home')
def index():
    return render_template('index.html')

@app.route('/user/register',endpoint='register')
def userReg():
    return render_template('user/register.html',default='')


@app.route('/user/login',endpoint='login',methods=['POST'])
def userLogin():
    # 验证 用户 名 和 密码是否正确
    print(request.form)
    return '用户登录成功'

@app.route('/user/register/entry', endpoint='entry',methods=['POST'])
def userEntry():
    print(request.form)

    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        port=3306,
        db='py301db',
        charset='utf8'
    )

    cursor = conn.cursor()
    sql = '''CREATE TABLE IF NOT EXISTS %s(
        id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        UID VARCHAR(256) NOT NULL,
        UPASS VARCHAR(18) NOT NULL,
        ULT VARCHAR(14),
        URT VARCHAR(14) NOT NULL,
        UTOKEN VARCHAR(256),
        USEX CHAR(1)
    )ENGINE=InnoDB DEFAULT CHARSET='UTF8';
    '''
    sql = sql % ('susers')
    cursor.execute(sql)

    # 插入任何数据之前必须 先查一下
    sql = '''select UID from susers where UID=%s;'''
    sql = sql % (request.form['uid'])
    cursor.execute(sql)
    rows = cursor.fetchall()
    if len(rows) !=0 :
        return render_template('user/register.html',default=request.form['uid'])


    # 如果没有就插入新数据
    sql = '''insert into susers(UID,UPASS,URT) values(
        %s,%s,%s);
    '''
    sql = sql % (request.form['uid'],request.form['upass'],'201903051551')
    cursor.execute(sql)
    conn.commit()
    
    cursor.close()
    conn.close()

    return redirect(url_for('home'))

import hashlib
@app.route('/safe')
def safe():
    password = '1234567812321321321'
    # 加密
    sha1 = hashlib.sha3_256()
    sha1.update(password.encode('utf-8'))
    new_pwd = sha1.hexdigest()
    print(new_pwd)
    # md5

    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    new_pwd = md5.hexdigest()
    print(new_pwd)


    return '1111'

from werkzeug.security import generate_password_hash,check_password_hash
@app.route('/safe2')
def safe2():
    pwd = 'abc123456'
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    new_pwd = md5.hexdigest()
    print('md5:',new_pwd)
    pwd_hash1 = generate_password_hash(new_pwd)
    print(pwd_hash1)
    new_str = 'abc123456'
    md52 = hashlib.md5()
    md52.update(new_str.encode('utf-8'))
    new_md5 = md52.hexdigest()
    print('md5:',new_md5)
    print(check_password_hash(pwd_hash1,new_md5))
    return '11223344'

import base64
def safe_base64_decode(s):
    print(s + b'=' * 3)
    return base64.b64decode(s + b'=' * 3)

@app.route('/b64')
def b64():
    image_name = 'zhengzhou.png'
    encode64 = base64.b64encode(image_name.encode('utf-8'))
    print(encode64)
    print(base64.b64decode(encode64))
    print(str(base64.b64decode(encode64),'utf-8'))
    return encode64


if __name__ == '__main__':
    app.run(debug=True)
    