# 这是一个 ORM 中的M 汽车的类对应 数据库中汽车表
from default import db

class Car(db.Model):
    __tablename__ = 'car'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    cname = db.Column(db.String(10),nullable=False)
    cengine = db.Column(db.String(10),nullable=False)

    def __init__(self,cname=''):
        self.cname = cname
    
    def __repr__(self):
        return '<Car %r,%r>'%(self.id,self.cname)

    def save(self):
        db.session.add(self)
        db.session.commit()
        