import pymysql
from pymysql import OperationalError,ProgrammingError


opt = {
        'host':'localhost',
        'user':'root',
        'password':'123456',
        'port':3306,
        'db':'py301db',
        'charset':'utf8'
}

#增删改查


def connectDB(**conf):
    try:
        connect_db = pymysql.connect(**conf)
        return connect_db
    except OperationalError as e:
        print(e)


# 查
# 1.全查
# 2.字段查
# 3.条件查
# 4.多表联查

#1.全表查
def queryFind(tableName='',cols='*',where=''):
    # 为了安全 保护代码执行
    # if tableName is None:
    #     return None
    
    connect = connectDB(**opt)
    if connect:
        cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            if where:
                sql = "select %s from %s where %s;" % (cols,tableName,where)
                print(sql)
            else:
                sql = "select %s from %s;" % (cols,tableName) 
            cursor.execute(sql)
            rows = cursor.fetchall()
            if rows:
                return rows
            else:
                return None
        except ProgrammingError as e:
            print(e)
            connect.rollback()
        finally:
            cursor.close()
            connect.close()
# insert into tableName(cols...) values(values....);



def queryInsert(tableName="",**kargs):
    #print(kargs.keys())
    #print(kargs.values())
    #print(','.join(str(i) for i in list(kargs.keys())))
    if len(list(kargs.keys())) == 0 or len(list(kargs.values())) == 0:
        return None
    
    if len(list(kargs.keys())) != len(list(kargs.values())):
        return None

    # 先把 column 列 和 值 要组织
    cclos = ','.join(str(i) for i in list(kargs.keys()))
    # uid=12345 and upass=12344
    totle_string = ''
    for i in range(len(list(kargs.keys()))):
        keys = list(kargs.keys())
        values = list(kargs.values())
        temp = keys[i] + '=' + values[i]
        totle_string += (temp + ' and ')

    rows = queryFind(tableName='susers',cols=cclos,where=totle_string[0:-5])
    if rows:
        print(rows)
    else:
        print('not find')


    return None
    # 先查

    # 么有匹配到就插入新值
    connect = connectDB(**opt)
    if connect:
        cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
        if cursor:
            try:
                cols = ','.join(str(i) for i in list(kargs.keys()))
                values = ','.join(str(i) for i in list(kargs.values()))
                sql = 'insert into %s(%s) values(%s);' % (tableName,cols,values)
                cursor.execute(sql)
                connect.commit()
                return True
            except Exception as e:
                print(e)
                connect.rollback()
                return None
            finally:
                cursor.close()
                connect.close()
        else:
            return None
    else:
        return None
    

        


if __name__ == '__main__':
    # opt = {
    #     'host':'localhost',
    #     'user':'root',
    #     'password':'123456',
    #     'port':3307,
    #     'db':'py301db',
    #     'charset':'utf8'
    # }
    # con = connectDB(**opt)
    # print(con)
    '''
    rows = queryFind(tableName='susers')
    if rows:
        pri
        print('not find')
    rows = queryFind(tableName='susers',cols='id,uid',where='id=2')
    if rows:
        print(rows)
    else:
        print('not find')
    '''
    data = {'uid':'10987654328','upass':'12345678','urt':'201903061717'}
    queryInsert(tableName='susers',**data)
    # rows = queryFind(tableName='susers',cols='id,uid')
    # if rows:
    #     print(rows)
    # else:
    #     print('not find')