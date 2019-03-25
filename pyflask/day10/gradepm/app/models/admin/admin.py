from sqlalchemy import Column,Integer,String,ForeignKey
from app.extensions import db
from werkzeug.security import generate_password_hash,check_password_hash
from app.models.role.role import Role


class Admin(db.Model):
    id = Column(Integer,primary_key=True,autoincrement=True)
    aid = Column(String(14),nullable=False,unique=True)
    aname = Column(String(128),nullable=False,unique=True)
    aemail = Column(String(256),nullable=False,unique=True)
    apasswd = Column(String(128),nullable=False)
    rid = Column(Integer, ForeignKey('role.id'))

    #用户头像

    #反向关系

    def __init__(self,aid='',aname='',aemail='',apasswd='',rid=0):
        self.aid = '+86' + aid
        self.aname = aname
        self.aemail = aemail
        # self.apasswd = apasswd
        # 通过 加盐哈希 对密码进行加密
        self.apasswd = generate_password_hash(apasswd)
        self.rid = rid

    # 数据库里面有些属性 是只读的 如何实现？？？

    def __repr__(self):
        return '<Admin %r>' % self.aid

    # 修改密码
    def resetPW(self,new_pw):
        self.apasswd = new_pw
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def verifyPW(self,pw):
        return check_password_hash(self.apasswd,pw)
    
    


