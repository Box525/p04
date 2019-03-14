from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app3 import app
from default import db
from car import Car

manager = Manager(app)

migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
