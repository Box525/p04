from app.extensions import db
from sqlalchemy import Column,Integer,String,ForeignKey
from app.models.gleader.gleader import GLeader

class Grade(db.Model):
    __tablename__ = 'grade'
    id = Column(Integer,primary_key=True,autoincrement=True)
    gid = Column(String(20), nullable=False,unique=True)
    gname = Column(String(20), nullable=False)
    # gleader = Column(String(20), nullable=False)
    lid = Column(Integer, ForeignKey('gleader.id'))
    leaders = db.relationship('GLeader',backref='grades')

    def __init__(self,gid='',gname='',gleader=''):
        self.gid = gid
        self.gname = gname
        self.gleader = gleader

    def __repr__(self):
        return '<Grade %r,%r,%r,%r>' % (self.id,self.gid,self.gname,self.gleader)

    def save(self):
        db.session.add(self)
        db.session.commit()
