from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from database import db_session
import PIL.Image as Image
import numpy as np
import io
import base64


# pip install Flask-WTF
class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


app = Flask(__name__)


@app.route('/add/<username>')
def add(username):
    print('hello', username)
    return render_template('hello.html', name=username)


@app.route('/projects/')
def projects():
    return 'project'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # user = User(form.username.data, form.email.data,
        #             form.password.data)
        print('user', form.username.data)
        # db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/about')
def aboult():
    return 'about'


@app.route('/child/')
def child1():
    return render_template('child1.html')


def get_data_uri(img):
    im = Image.fromarray(img)  # numpy 转 image类
    output_buffer = io.BytesIO()
    im.save(output_buffer, format='JPEG')
    # extension = filename.split(".")[-1].lower()
    mime_type = "image/jpeg"
    content = base64.b64encode(output_buffer.getvalue())
    content = content.decode(encoding="utf-8")
    return "data:%s;base64,%s" % (mime_type, content)


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    print('method', request.method)
    if request.method == 'POST':
        print('post')
        data = {}
        data['code'] = -1
        for f in request.files:
            file = request.files[f]
            img = Image.open(file.stream)
            img = img.convert('RGB')
            img = np.array(img)
            # key就是file，1.png
            print(img.shape, f, file.filename, type(file))
            # png是4个channel，需要转为rgb
            # werkzeug.datastructures.FileStorage
            # 有save
            data['img'] = get_data_uri(img)
            data['result'] = 'good'
            return jsonify(data)

    return render_template('upload.html')


@app.route('/show/', methods=['post'])
def show():
    print(request.method)
    f = request.files['file']
    print(type(f))
    return 'ok'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(port=5002, debug=True)
