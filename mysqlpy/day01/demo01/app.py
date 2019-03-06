import pymysql

# 创建连接 连接数据库
conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password='123456',
    db='py301db',
    charset='utf8'
)

# 操作 数据库
# 需要一个对象 这个对象称之为 游标
cursor = conn.cursor() # 返回的是一个元组 

#删除users表中数据
# cursor.execute("delete from users")
cursor.execute("truncate table users")
#提交
conn.commit()

# 增加一条数据
sql = '''
insert into users(uname,uage) values(%s,%s)
'''

# 执行SQL 语句
cursor.execute(sql,('IG.王校长',30))

# 必须提交 切记是 conn 对象提交
conn.commit()

# 操作数据库之前必须 配置好 MySQL 语句
sql = '''
select * from users;
'''

# 执行SQL 语句
# 数据操作统统都是需要使用游标对象进行操作
cursor.execute(sql)

# 获取select 结果是通过
res = cursor.fetchall()
print(res)

# 必须释放首先要关闭游标
cursor.close()

# 关闭连接
conn.close()
