from app.extensions import db
from sqlalchemy import Column, Integer, String, SmallInteger,ForeignKey
from app.models.role.role import Role

class GLeader(db.Model):
    __tablename__ = 'gleader'
    id = Column(Integer,primary_key=True,autoincrement=True)
    lphone = Column(String(11), nullable=False, unique=True)
    lname = Column(String(20),nullable=False)
    lemail = Column(String(256), nullable=False, unique=True)
    lsex = Column(SmallInteger,nullable=False)
    lpw = Column(String(18),default='666666')
    rid = Column(Integer, ForeignKey('role.id'))

    def __init__(self,lphone='',lname='',lemail='',lsex=0,rid=0):
        self.lphone = lphone
        self.lname = lname
        self.lemail = lemail
        self.lsex = lsex
        self.rid = rid

    def __repr__(self):
        return '<GLeader %r>' % (self.lphone)

    def save(self):
        db.session.add(self)
        db.session.commit()


