from flask import Flask,url_for,render_template,redirect,request
import pymysql


app = Flask(__name__)


# 连接数据库
def conDB():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        db='py301db',
        port=3306,
        charset='utf8')
    return conn


def createCursor(con):
    return con.cursor()


def querySQL(sql_string, con):
    new_cursor = con.cursor()
    new_cursor.execute(sql_string)
    # rows = new_cursor.fetchall()
    # print(rows)
    return new_cursor


def closeCursor(cur):
    cur.close()


def closeConnect(con):
    con.close()


def main():
    """
    # 数据库连接
    conn = conDB()
    # 创建游标
    cursor = createCursor(conn)

    # 创建表
    sql = '''create table if not exists students(
        id int unsigned auto_increment primary key,
        uname varchar(128) not null,
        uage tinyint unsigned not null
        )engine=InnoDB charset='utf8';
        '''

    querySQL(sql,conn)
    closeCursor(cursor)
    closeConnect(conn)
    """

    print(app.view_functions)
    print(app.url_map)
    app.run(debug=True)


@app.route('/')
def index():
    # 显示主页 总的数据操作 CRUD
    return render_template('index.html')

@app.route('/create/', endpoint='ctable')
def createDBTable():
    return render_template('create.html')

@app.route('/create/table')
def createTable():
    msg = {
        'title': '系统提醒',
        'error': ''
    }

    # pymysql 在python中的操作步骤：
    '''
        1.创建MySQL的连接
        2.生产游标进行MySQL操作
        3.执行SQL语句
        4.关闭连接
    '''
    conn = conDB()
    curosr = createCursor(conn)
    sql = '''create table if not exists %s(
        id int unsigned auto_increment primary key,
        uname varchar(128) not null,
        uage tinyint unsigned not null,
        usex char not null,
        uphone char(14) not null
    )engine=InnoDB default charset='utf8';
    '''
    get_table_name = request.args.get('tname')
    if get_table_name:
        sql = sql % get_table_name
    else:
        closeCursor(curosr)
        closeConnect(conn)
        msg.error = '数据库操作失败，表创建失败'
        return render_template('info.html',msg=msg)

    querySQL(sql,conn)
    closeCursor(curosr)
    closeConnect(conn)

    return render_template('info.html',msg=msg)

@app.route('/search/')
def search():
    return render_template('search.html')

@app.route('/add/')
def add():
    # 4步
    conn = conDB()
    curosr = createCursor(conn)
    sql = "select column_name from information_schema.columns where table_name='%s' and table_schema='%s';"
    sql = sql % ('students','py301db')
    # print(sql)
    # sql = '''select * from students'''

    curosr = querySQL(sql, conn)
    rows = curosr.fetchall()
    closeCursor(curosr)
    closeConnect(conn)
    return render_template('add.html',rows=rows)


@app.route('/add/one',endpoint='addone')
def addOne():
    print(list(request.args.keys()))
    print(list(request.args.values()))
    return 'add ok!!!!'


if __name__ == '__main__':
    main()
