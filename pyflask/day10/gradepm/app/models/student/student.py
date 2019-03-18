from app.extensions import db
from sqlalchemy import Column, Integer, String, DateTime


class Student(db.Model):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sid = Column(String(20), nullable=False, unique=True)
    sname = Column(String(20), nullable=False)
    ssex = Column(Integer, nullable=False)
    gid = Column(Integer, db.ForeignKey('grade.id'))
    students = db.relationship('Grade',backref='students')

    def __init__(self, sid='', sname='', ssex=0,gid=0):
        self.sid = gid
        self.sname = gname
        self.ssex = ssex
        self.gid = gid


    def __repr__(self):
        return '<Student %r,%r,%r,%r,%f>' % (self.id, self.sid, self.sname,self.ssex,self.gid)

    def save(self):
        db.session.add(self)
        db.session.commit()