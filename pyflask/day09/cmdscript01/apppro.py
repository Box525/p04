from flask import Flask
from ext import db
import config

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

# with app.app_context():
#     db.create_all()

@app.route('/')
def index():
    return '使用命令来操作flask 应用!!!!'

@app.route('/car')
def car():
    return 'car  car  car!!'


if __name__ == '__main__':
    app.run(debug=True)
    