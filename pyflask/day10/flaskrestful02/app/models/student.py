from app.ext import db
from sqlalchemy import Column,Integer,String,DateTime

class Student(db.Model):
    '''学生数据模型'''
    id = Column(Integer,primary_key=True,autoincrement=True)
    sno = Column(String(18),nullable=False,unique=True)
    sname = Column(String(16),nullable=False)
    ssex = Column(Integer)

    __tablename__ = 'student'

    def __init__(self,sno='',sname='',ssex=0):
        self.sno = sno
        self.sname = sname
        self.ssex = ssex
    
    def __repr__(self):
        return '<Student %r,%r,%r,%r>' % (self.id,self.sno,self.sname,self.ssex)

    def save(self):
        db.session.add(self)
        db.session.commit()