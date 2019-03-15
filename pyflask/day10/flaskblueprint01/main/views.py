from . import main
from flask import render_template,redirect,url_for
from models.student import Student


@main.route('/',endpoint='home2')
def index():
    stu = Student(sname='doubendou')
    print(stu)
    return render_template('index.html')

@main.route('/main/')
def main2():
    return 'main url'

@main.route('/main2')
def home():
    return redirect(url_for('.home2'))