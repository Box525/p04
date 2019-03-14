from flask_script import Manager

DBManager = Manager()

@DBManager.command
def init():
    print('数据库初始完毕')

@DBManager.command
def migrate():
    print('数据库迁移成功')

@DBManager.command
def upgrade():
    print('数据更新')