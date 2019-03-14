from flask import Flask

from scoremodel import Score
from dbetc import db
import config

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def idnex():
    # 增加数据
    python = Score(classname='java',sc=90)
    # 事务操作
    db.session.add(python)
    db.session.commit()
    print(python)
    return 'index'

if __name__ == '__main__':
    app.run(debug=True)