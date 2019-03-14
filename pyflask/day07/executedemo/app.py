from flask import Flask
import pymysql

app = Flask(__name__)


config = {
    'host':'127.0.0.1',#localhost
    'user':'root',
    'passwd':'123456',
    'port':3306,
    'charset':'utf8',
    #'db':'py301db',
    'cursorclass':pymysql.cursors.DictCursor
}

connect = pymysql.connect(**config)
# 事务操作 自动提交
connect.autocommit(1)

# 创建游标
cursor = connect.cursor()

try:
    # 创建数据库
    DB_NAME = 'py302db'
    cursor.execute('DROP DATABASE IF EXISTS %s' %DB_NAME)
    cursor.execute('CREATE DATABASE IF NOT EXISTS %s' %DB_NAME)
    connect.select_db(DB_NAME)

    # 创建表
    TABLE_NAME = 'user'
    cursor.execute('CREATE TABLE %s(id int unsigned auto_increment primary key,name varchar(30))engine=InnoDB default charset=utf8;' %TABLE_NAME)

    # 插入1条数据
    # sql = 'INSERT INTO %s VALUES(%s)' %(TABLE_NAME,'Tom')
    # 不建议直接拼sql 语句，占位符会引发 注入（防注入）
    # execute 提供了直接传值的方式，防止注入
    # value = ['Tom233']
    value = ('Tom244')
    cursor.execute('INSERT INTO '+ TABLE_NAME + ' values(null,%s)',value)
    
    #批量插入
    values = []
    for i in range(1000):
        values.append(('Tom' + str(i)))
    cursor.executemany('INSERT INTO '+ TABLE_NAME + ' values(null,%s)',values)

    


except:
    import traceback
    traceback.print_exc()
    # 发生错误 回滚
    connect.rollback()
finally:
    #关闭游标
    cursor.close()
    #关闭连接
    connect.close()
    



@app.route('/')
def index():
   return 'home'


if __name__ == '__main__':
    app.run(debug=True)
    

