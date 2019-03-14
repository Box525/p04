from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '使用命令来操作flask 应用!!!!'


if __name__ == '__main__':
    app.run(debug=True)
    