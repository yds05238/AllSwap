'''
  __init__.py
  Backend Development Team

  Code that intializes the application. 
'''
from flask import Flask, request, render_template, url_for
import json
from db import db, User, Data
from os import path 

db_filename = "data.db"
app = Flask(__name__)

#app.config.from_object('config')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' %db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
with app.app_context():
  db.create_all()

@app.route('/')
def index():
  return render_template("templates/index.html", result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

