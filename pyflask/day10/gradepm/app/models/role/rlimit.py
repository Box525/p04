from app.extensions import db
from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.role.role import Role
from app.models.role.rl import rl

class RLimit(db.Model):
    id = Column(Integer,primary_key=True,autoincrement=True)
    rlname = Column(String(20),nullable=False,unique=True)
    # rid = Column(Integer, ForeignKey('role.id'))
    #secondary 指明附表名
    limits = db.relationship('Role',secondary=rl,backref='limits')


    __tablename__ = 'limittable'

    def __init__(self, rlname=''):
        self.rlname = rlname
        # self.rid = rid

    def __repr__(self):
        return '<Limit %r>' % self.rlname

    def save(self):
        db.session.add(self)
        db.session.commit()
