from flask import Flask
from flask_restful import Api
from app.urlapi import Student
from app.models.student import Student as Stu
from app.ext import db
import config


app = Flask(__name__)
app.config.from_object(config)
app.debug = True
api = Api(app)
db.init_app(app)

api.add_resource(Student,'/student')



if __name__ == '__main__':
    app.run()
    