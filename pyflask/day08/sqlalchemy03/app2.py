from flask import Flask
from default import db
from car import Car
import config

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

# db.create_all()
with app.app_context():
    db.create_all()

@app.route('/')
def index():

    return 'app2.py'


if __name__ == '__main__':
    app.run(debug=True)
    