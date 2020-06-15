from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home:')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
