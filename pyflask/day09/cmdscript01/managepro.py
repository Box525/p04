from flask_script import Manager
from apppro import app
from flask_migrate import Migrate,MigrateCommand
from ext import db
from car import Car
from student import Student

manager = Manager(app)

#MigrateCommand 用来处理表迁移的命令
# init
# migrate
# upgrade
# 模型-----》 迁移文件 ----》 表

#1. 如果想实现迁移 必须绑定app 和 db
migrate = Migrate(app,db)

#2. 把 扩展写好的 MigrateCommand 添加在manager中
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run(default_command='runserver')
    