from ext import db
from sqlalchemy import Column,Integer,String

class Student(db.Model):
    id = Column(Integer,primary_key=True,autoincrement=True)
    sname = Column(String(100),nullable=False)

    def __init__(self,sname=''):
        self.sname = sname
    
    def __repr__(self):
        return '<Car %r,%r>'%(self.id,self.sname)
    
    def save(self):
        db.session.add(self)
        db.session.commit()