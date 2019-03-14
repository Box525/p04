from ext import db
from sqlalchemy import Column,Integer,String

class Car(db.Model):
    id = Column(Integer,primary_key=True,autoincrement=True)
    cname = Column(String(100),nullable=False)

    def __init__(self,cname=''):
        self.cname = cname
    
    def __repr__(self):
        return '<Car %r,%r>'%(self.id,self.cname)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

