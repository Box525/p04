from flask import Flask, url_for, request, render_template, redirect,make_response

app = Flask(__name__, template_folder="html")


@app.route('/')
def index():
    return render_template('index.html', title='首页')

# /lgoin?token=value
@app.route('/login')
def login():
    print(request.args)
    print(request.method)
    return render_template('login.html')


@app.route('/user', methods=['POST'])
def user_login():
    print(url_for('index'))
    print(url_for('login'))
    return redirect(url_for('index'))


@app.route('/setcookie', endpoint='setcookie', methods=['GET', 'POST'])
def setCookie():
    return render_template('setcookie.html')

@app.route('/cookie/set', methods=['GET', 'POST'])
def cookieSet():


    val = request.args.get('setcookie')

    cval = request.cookies.get('uuid')
    if cval:
        val = val + cval
    else:
        val = val + '00000000000'


    resp = make_response(render_template('index.html'))
    resp.set_cookie('uuid',val)
    return resp

@app.errorhandler(404)
def page404(e):
    return render_template('404.html'),404


def main():
    print(app.view_functions)
    print(app.url_map)
    app.run(debug=True)


if __name__ == '__main__':
    main()
