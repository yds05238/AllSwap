'''
  db.py
  AllSwap Backend Development Team

  Database Structure for AllSwap web application.
'''
from flask_sqlalchemy import SQLAlchemy 
from app import login
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

class User(db.Model):
    # ...

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader 
def load_user(id):
    return User.query.get(int(id))

