'''
如果想使用多对多
需要定义一个用于关系的辅助表
对于这个辅助表不使用模型
而是采用一个实际的表

'''
from app.extensions import db
from sqlalchemy import Column,Integer,ForeignKey
# from app.models.role.role import Role
# from app.models.role.rlimit import RLimit
rl = db.Table('rl',
              Column('rid', Integer, ForeignKey('role.id'), primary_key=True),
              Column('lid', Integer, ForeignKey('limittable.id'),primary_key=True)
              )
