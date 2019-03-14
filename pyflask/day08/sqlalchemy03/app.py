from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

'''
班级表
create table grade(
    gid #班级id
    gname #班级名称
)
学生表
create table student(
    sid #学生id
    sname #学生姓名
    gid # 外键
)
'''

class Grade(db.Model):
    __tablename__ = 'grade'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    gid = db.Column(db.String(10),nullable=False)
    gname = db.Column(db.String(128),nullable=False)

    def __init__(self,gid='',gname=''):
        self.gid = gid
        self.gname = gname

    def __repr__(self):
        return '<Grade %r,%r,%r>'%(self.id,self.gid,self.gname)

    def save(self):
        db.session.add(self)
        db.session.commit()

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    sid = db.Column(db.String(6),nullable=False)
    sname = db.Column(db.String(128),nullable=False)
    gid = db.Column(db.Integer,db.ForeignKey('grade.id'))
    grade = db.relationship('Grade',backref=db.backref('students'))

    def __init__(self,sid='',sname='',gid=0):
        self.sid = sid
        self.sname = sname
        self.gid = gid

    def __repr__(self):
        return '<Student %r,%r,%r,%r>'%(self.id,self.sid,self.sname,self.gid)

    def save(self):
        db.session.add(self)
        db.session.commit()


db.create_all()

@app.route('/')
def index():
    # a_grade = Grade(gid='10001',gname='卓越班')
    # a_grade.save()

    # a_grade = Grade.query.filter(Grade.gname == "卓越班").first()
    # if a_grade:
    #     xiao_fang = Student(sid='00002',sname='马云',gid=a_grade.id)
    #     xiao_fang.save()
    # else:
    #     return 'not fount 班级'

    a_grade = Grade.query.filter(Grade.gname == "卓越班").first()
    res = a_grade.students
    print(res)



    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
    