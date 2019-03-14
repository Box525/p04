from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_,not_,and_
import config
app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

class Score(db.Model):
    __tablename__ = 'score'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    cname = db.Column(db.String(100),nullable=False)
    sc = db.Column(db.Float,default=0.0)

    def __init__(self,cname='',sc=0.0):
        self.cname = cname
        self.sc = sc
    
    def __repr__(self):
        return '<Score %r,%r,%r>' %(self.id,self.cname,self.sc)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

db.create_all()

@app.route('/')
def index():
    # #增加1个
    # python = Score(cname='python',sc=85.5)
    # db.session.add(python)
    # db.session.commit()
    # print(python)

    # #增加多个
    # java = Score(cname='java',sc=75.5)
    # net = Score(cname='.net',sc=70.2)
    # php = Score(cname='php',sc=81.1)
    # scores = []
    # scores.append(java)
    # scores.append(net)
    # scores.append(php)

    # #批量插入
    # db.session.add_all(scores)
    # db.session.commit()

    # # 查
    # # select * from tablename;
    # # 全查
    # result = Score.query.filter().all()
    # print(result[0].cname)
    # # 带条件查
    # result = Score.query.filter(or_(Score.sc > 80,Score.cname == 'php')).all()
    # print(result)

    # # 删
    # # get(表的主键的值)
    # python = Score.query.get(4)
    # # db.session.delete(python)
    # # db.session.commit()
    # python.delete()

    # # 改
    # result = Score.query.all()[0]
    # net = Score.query.get(result.id)
    # print(net)
    # net.delete()

    # # 高级查
    # # 比较查询
    # # 小于 __lt__() 小于等于__le__() 大于 __gt__ 大于等于 __ge__
    # res = Score.query.filter(Score.sc.__le__(80))
    # print(res)

    # # in_查询
    # res = Score.query.filter(Score.sc.in_([80,90]))
    # print(res)

    # 排序
    # order_by(字段名称.asc()) #asc()升序，desc()降序 默认升序
    # res = Score.query.order_by(Score.sc.asc()).all()
    # print(res)
    res = Score.query.filter(Score.sc.__gt__(75)).order_by(Score.sc.asc()).all()
    print(res)

    # 多条件查询
    # sqlalchemy 的方法 and_(条件,条件2,...) or_(条件,条件2,...) not_(条件,条件2,...)
    result = Score.query.filter(or_(Score.sc > 80,Score.cname == 'php')).all()
    print(result)
    return 'index'

    


if __name__ == '__main__':
    app.run(debug=True)
