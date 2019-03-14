from flask import Flask
#1.1 导入 flask-sqlalchemy 
from flask_sqlalchemy import SQLAlchemy

#1.3 导入config 配置文件
import config

app = Flask(__name__)
# 1.4 使用配置文件
app.config.from_object(config)
# dialect+driver://username:password@host:port/database?charset=utf8
#1.2 使用 flask-sqlalchemy
# 初始化数据库对象
db = SQLAlchemy(app)

# '''成绩表'''
# create table score(
#     id int primary key auto_increment,
#     classname varchar(100) not null,
#     sc int not null
# )

class Score(db.Model):## 继承SQLAlchemy.Model对象，一个对象代表了一张表
    __tablename__ = 'score'  # 该参数可选，不设置会默认的设置表名，如果设置会覆盖默认的表名
    # id 整型，主键，自增，唯一
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    # 名字 字符串长度为100 非空
    classname = db.Column(db.String(100),nullable=False)
    # 成绩 整型，默认为0
    sc = db.Column(db.Integer, default=0)
    

    # 初始化方法，可以对对象进行创建
    def __init__(self,classname='',sc=0):
        self.classname = classname
        self.sc = sc
    # 输出方法，与__str__类似，但是能够重现它所代表的对象
    def __repr__(self):
        return '<Score %r,%r,%r>' %(self.id,self.classname,self.sc)

# 以上就是 sqlalchemy 的基本使用方式 测试：
db.create_all()


@app.route('/')
def idnex():
    # 增加数据
    python = Score(classname='java',sc=90)
    # 事务操作
    db.session.add(python)
    db.session.commit()
    print(python)
    return 'index'

if __name__ == '__main__':
    app.run(debug=True)
    