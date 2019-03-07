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

class User(db.Model):
  """A user of the web application.

  :param int id: Unique id for the user
  :param str email: email address of the user 
  :param str password: encrypted password for the user
  :param int rating: integer rating of user
  :param products: The user's products for sale
  :param bids: The user's bids. 
  """
  __tablename__ = 'user'

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String, unique=True, nullable=False)
  password = db.Column(db.String, unique=True, nullable=False)
  rating = db.Column(db.Integer, nullable=False)
  products = db.relationship('Product', cascade= 'delete')
  bids = db.relationship('Bid', cascade= 'delete')

  def __init__(self, **kwargs):
    self.email = kwargs.get('email', '')
    self.username = kwargs.get('username', '')
    self.rating = kwargs.get('rating', '')
  
  def serialize(self):
    return {
      'id': self.id,
      'email': self.email,
      'password': self.password,
      'rating': self.rating
    }

class Product(db.Model):
  """Product for sale on the website.
  
  :param int id: Unique id for this product
  :param str name: name of this product
  :param str email: email of the seller
  :param int price: price of the product
  :param DateTime timestamp: time the product was put up for sale
  :param int user_id: id of the seller 
  :param bids: The bids placed on this product.
  """

  __tablename__ = "product"
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  email = db.Column(db.String, db.ForeignKey('user.email'), nullable=False)
  price = db.Column(db.Integer, nullable=False)
  timestamp = db.Column(db.DateTime, default = datetime.now)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  bids = db.relationship('Bid', cascade= 'delete')

  def __init__(self, **kwargs):
    self.name = kwargs.get('name', '')
    self.email = kwargs.get('email')
    self.price = kwargs.get('price', '')
    self.user_id = kwargs.get('user_id')
  
  def serialize(self):
    return {
      'id': self.id,
      'name': self.name, 
      'email': self.email,
      'price': self.price,
      'timestamp': self.timestamp
    }

  def __str__(self):
        """Return the string representation of the product sale."""
        return '{} sold by {}'.format(self.name, self.email)

class Bid(db.Model):
  """Bid placed on the product for sale.

  :param int id: Unique id for this bid
  :param int amount: amount of cash placed in the bid
  :param int timestamp: time the bid was created
  :param str buyer_email: email of the user who places this bid
  :param int product_id: id of the product the bid is placed on
  :param int buyer_id: id of the user who places this bid.
  """

  __tablename__ = "bid"

  id = db.Column(db.Integer, primary_key=True)
  amount = db.Column(db.Integer, nullable=False)
  timestamp = db.Column(db.DateTime, default=datetime.now)
  buyer_email = db.Column(db.String, db.ForeignKey('user.email'), nullable=False)
  product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
  buyer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  def __init__(self, **kwargs):
    self.amount = kwargs.get('amount', '0')
    self.buyer_email = kwargs.get('user_email')
    self.product_id = kwargs.get('product_id')
    self.buyer_id = kwargs.get('user_id')
  
  def serialize(self):
    return {
      'id': self.id,
      'amount': self.amount,
      'timestamp': self.timestamp,
      'buyer_email': self.seller_email
    }
  
  def __str__(self):
    """Return the string representation of the bid placed."""
    return '{} dollar bid placed by {}'.format(self.amount, self.buyer_email)



  