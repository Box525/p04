import pymysql
import time
from functools import wraps

# 数据库配置信息
PYMYSQL_CONFIG = {
    'host':'127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': '123456',
    'db': 'py301db',
    'charset': 'utf8'
}

# 当前时间
def now():
    return time.time()

# 计算 函数 执行的时间
def fnTimer(fn):
    @wraps(fn)
    def functionTimer(*args,**kwargs):
        start = now()
        result = fn(*args,**kwargs)
        print('{%s} total running time {%f} seconds' %(fn.__name__,now()-start))
        return result
    return functionTimer

'''
create table info(
    email,
    password
)

'''

# 插一条数据
@fnTimer
def testExecute(connection,sql):
    # 数据库操作
    row_count = 0
    with connection.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
        for i in range(1000):
            row_count += cursor.execute(sql,('tim.apple@apple.com','test' + str(i)))
            connection.commit()
    return row_count


# 批量插入
@fnTimer
def testExecuteMany(connection,sql):
    with connection.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
        # [(),(),()]
        datas = [('jack.ali@ali.com','test' + str(i)) for i in range(1,1001)]
        row_count = cursor.executemany(sql,datas)
        connection.commit()
        return row_count

if __name__ == '__main__':
    insert_sql = 'INSERT INTO ss(email,passwd) values(%s,%s)'
    connection = pymysql.connect(**PYMYSQL_CONFIG)

    testExecute(connection,insert_sql)
    testExecuteMany(connection,insert_sql)
    


