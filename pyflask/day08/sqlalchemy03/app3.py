from flask import Flask
from default import db
import config
from car import Car
app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

@app.route('/')
def index():
    benz = Car(cname='奔驰')
    benz.save()
    baoma = Car(cname='宝马')
    baoma.save()
    return 'app33333.py'


if __name__ == '__main__':
    app.run(debug=True)