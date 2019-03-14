# 用来管理当前的app 分离功能  应用和数据库
# 采用 命令的方式来进行 操作
# flask-script 就是用来操作命令

from flask_script import Manager
from app import app
from db_script import DBManager

manager = Manager(app)

@manager.command
def haodong():
    print('haodong cmd!!!!')


manager.add_command('db',DBManager)

if __name__ == '__main__':
    manager.run()
    