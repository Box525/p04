from flask import Flask
from main import main as main_view

app = Flask(__name__)

app.register_blueprint(main_view)

# @app.route('/')
# def index():
#     return 'home'

if __name__ == '__main__':
    print(app.url_map)
    print(app.view_functions)
    app.run(debug=True)
    