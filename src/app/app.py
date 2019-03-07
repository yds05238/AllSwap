'''
    app.py 
    AllSwap Backend Development Team

    Code for backend routes.
'''
import json
from flask import Flask, request, render_template
from db import db 
#from db import db 
from os import path 
#from flask_login import LoginManager, current_user, login_user, logout_user, login_required

db_filename = "data.db"
app = Flask(__name__)
db.init_app(app)

CLIENT_HOST = '0.0.0.0'
PORT = 5000

#app.config.from_object('config')
#login = LoginManager(app)
#login.login_view = 'login'


'''
db.init_app(app)
with app.app_context():
    db.create_all()
'''
@app.route('/')
def index():
    return render_template("index.html"), 200
"""
@app.route('/index')
@login_required
def index():
    return render_template("index.html"), 200

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

"""

if __name__ == '__main__':
    app.run(host=CLIENT_HOST, port=PORT, debug=True)
