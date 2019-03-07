'''
  db.py
  AllSwap Backend Development Team

  Database Structure for AllSwap web application.
'''
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime 
#from app import login
#from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
"""
class User(db.Model):
  A user of the web application.

  :param int id: Unique id for the user
  :param str email: email address of the user 
  :param str password: encrypted password for the user
  :param int rating: integer rating of user
  :param products: The user's products for sale
  :param bids: The user's bids. 
  
  
  __tablename__ = "user"

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String, unique=True, nullable=False)
  password = db.Column(db.String, unique=True, nullable=False)
  rating = db.Column(db.Integer, nullable=False)
  bid_id = db.Column(db.Integer, db.ForeignKey('bid.id'), nullable = False)
  product_id = db.Column(db.Integer, db.ForeignKey('product.id', nullable=False) 

  def __init__(self, **kwargs):
    self.email = kwargs.get('email', '')
    self.username = kwargs.get('username', '')
    self.rating = kwargs.get('rating', '')
    self.product_id = kwargs.get('product_id', '')
    self.bid_id = kwargs.get('bid_id', '')

  def serialize(self):
    return {
      'id': self.id,
      'email': self.email,
      'password': self.password,
      'rating': self.rating
      'product_id': self.product_id,
      'bid_id': self.bid_id
    }
"""
class Product(db.Model):
  __tablename__ = "product"
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  price = db.Column(db.Integer, nullable=False)
  bids = db.relationship('Bid', cascade= 'delete')

  def __init__(self, **kwargs):
    self.name = kwargs.get('name', '')
    self.price = kwargs.get('price', 0)
  
  def serialize(self):
    return {
      'id': self.id,
      'name': self.name, 
      'price': self.price
    }

class Bid(db.Model):
  __tablename__ = "bid"

  id = db.Column(db.Integer, primary_key=True)
  amount = db.Column(db.Integer, nullable=False)
  product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

  def __init__(self, **kwargs):
    self.amount = kwargs.get('amount', '0')
    self.product_id = kwargs.get('product_id')
  
  def serialize(self):
    return {
      'id': self.id,
      'amount': self.amount
    }

