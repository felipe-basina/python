from flask import render_template, flash, redirect, url_for, jsonify
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user

@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'flasker'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    #return render_template('index.html', title='home', user=user)
    return render_template('index.html', user=user, posts=posts)

@app.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm(remember_me=True)
	if form.validate_on_submit():
		flash('Login for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign in', form=form)

@app.route("/ping")
def ping():
    return jsonify({'status': 'ok'})