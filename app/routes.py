from app import app
from flask import render_template
from app.forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Aisha'}
    posts = [
        {
            "author": {'username': 'Aisha'},
            "body": "You guys eat too much eba!"
        },
        {
            "author": {'username': 'Bolaji'},
            "body": 'I kuku watch game of thrones and I am fine yet.'
        },
    ]
    return render_template('index.html', user=user, posts=posts)
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)