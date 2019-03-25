from app.extensions import db
from sqlalchemy import Column, Integer, String, ForeignKey

class Role(db.Model):
    id = Column(Integer,primary_key=True,autoincrement=True)
    rname = Column(String(20),nullable=False,unique=True)

    def __init__(self,rname=''):
        self.rname = rname

    def __repr__(self):
        return '<Role %r>' % self.rname
    # name = name1;
    # sql = select * from user where name=name = name1; && pw=%s; % (name1,pw1)
    # res = execure(sql,)
    # if res : 

    def save(self):
        db.session.add(self)
        db.session.commit()
        