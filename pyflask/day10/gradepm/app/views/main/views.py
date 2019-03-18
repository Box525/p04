from . import main
from flask import render_template,url_for,redirect

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/favicon.ico')
def facicon():
    return ''