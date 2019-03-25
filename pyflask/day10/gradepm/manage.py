from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app import create_app
from app.extensions import db

from app.models.gleader.gleader import GLeader
from app.models.grade.grade import Grade
# from app.models.student.student import Student
from app.models.admin.admin import Admin
from app.models.role.role import Role
from app.models.role.rlimit import RLimit
from app.models.role.rl import rl

# 生产 app 对象
app = create_app()

manage = Manager(app)
migrate = Migrate(app,db)
manage.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manage.run(default_command='runserver')
