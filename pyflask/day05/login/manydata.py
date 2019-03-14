import pymysql
import time
from functools import wraps

# 数据库配置信息
SHOUFUYOU_USER_PROFILE_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'py301db',
    'charset': 'utf8',
}

def now():
    return time.time()

def fn_timer(fn):
    @wraps(fn)
    def function_timer(*args, **kwargs):
        start = now()
        result = fn(*args, **kwargs)
        print('{%s} total running time {%f} seconds' % (fn.__name__,now()-start))
        return result
    return function_timer

@fn_timer
def test_execute(connection, sql):
    rows_count = 0
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        for i in range(1000):
            rows_count += cursor.execute(sql, ('frank@python.org', 'test' + str(i)))
        connection.commit()

    return rows_count


@fn_timer
def test_execute_many(connection, sql):
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        datas = [('webmaster@python.org', 'test' + str(i)) for i in range(1,1000)]
        rows_count = cursor.executemany(sql, datas)
        connection.commit()

    return rows_count

if __name__ == '__main__':
    insert_sql = "INSERT INTO `p04data`(`email`, `password`) VALUES (%s, %s)"
    connection = pymysql.connect(**SHOUFUYOU_USER_PROFILE_CONFIG)

    test_execute(connection, insert_sql)
    test_execute_many(connection, insert_sql)

