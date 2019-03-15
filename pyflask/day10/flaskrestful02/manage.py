from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app.app import app
from app.ext import db
from app.models.student import Student

manage = Manager(app)

migrate = Migrate(app,db)

manage.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manage.run(default_command='runserver')
    
