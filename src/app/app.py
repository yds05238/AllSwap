'''
    app.py 
    AllSwap Backend Development Team

    Code for backend routes.
'''
from flask import Flask, request, render_template
import json
from db import db, Product, Bid
from os import path 
#from flask_login import LoginManager, current_user, login_user, logout_user, login_required

db_filename = "data.db"
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' %db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

CLIENT_HOST = '0.0.0.0'
PORT = 5000

db.init_app(app)
with app.app_context():
    db.create_all()

#app.config.from_object('config')
#login = LoginManager(app)
#login.login_view = 'login'

@app.route('/')
def test():
    return render_template('index.html'), 200

#Get all products
@app.route('/api/products/')
def get_all_products():
    products = Product.query.all()
    result = {"success": True, "data": [product.serialize() for product in products]}
    return json.dumps(result), 200

#Create a Product Posting
@app.route("/api/products/", methods=["POST"])
def create_product():
    if (request.data):
        product_body = json.loads(request.data)
        product = Product(
            name = product_body.get('name'),
            price= product_body.get('price')
        )
        db.session.add(product)
        db.session.commit()
        return json.dumps({"success": True, "data": product.serialize()}), 201
    else:
        return json.dumps({"success": False, "error": "Invalid POST request"}), 500

#Get a speific post 
@app.route('/api/product/<int:id>/')
def get_product(id):
    product = Product.query.filter_by(id=id).first()
    if product is not None:
        return json.dumps({"success": True, "data": product.serialize()}), 200
    return json.dumps({"success": False, "error": "Product not found..."}), 404

#Edit a Product Posting
@app.route('/api/product/<int:id>/', methods=["POST"])
def edit_product_price(id):
    if (request.data):
        product = Product.query.filter_by(id=id).first()
        if product is not None:
            product_body = json.loads(request.data)
            product.price = product_body.get('price', product.price)
            db.session.commit()
            return json.dumps({"success": True, "data": product.serialize()}), 201
        else:
            return json.dumps({"success": False, "error": "Produc not found..."}), 404
    else:
        return json.dumps({"success": False, "error": "Invalid POST request"}), 500


#Delete a specific product posting
@app.route("/api/product/<int:id>/", methods=["DELETE"])
def delete_product(id):
    product = Product.query.filter_by(id=id).first()
    if product is not None:
        db.session.delete(product)
        db.session.commit()
        return json.dumps({"success": True, "data": product.serialize()}), 200
    else:
        return json.dumps({"success": False, "error": "Product not found..."}), 404

#Get all bids of a specific product 
@app.route("/api/product/<int:id>/bids/")
def get_bids(id):
    product = Product.query.filter_by(id=id).first() 
    if product is not None:
        bids = [bid.serialize() for bid in product.bids]
        return json.dumps({"success": True, "data": bids}), 200
    else:
        return json.dumps({"success": False, "error": "Product not found..."}), 404

#create a bid posting
@app.route("/api/product/<int:id>/bid/", methods=["POST"])
def create_bid(id):
    if (request.data):
        product = Product.query.filter_by(id=id).first()
        if product is not None:
            product_body = json.loads(request.data)
            bid = Bid(
                amount = product_body.get('amount', 0),
                buyer_email = product_body.get('buyer_email'),
                product_id = product_body.get('product_id'),
                buyer_id = product_body.get('buyer_id')
            )
            product.bids.append(bid)
            db.session.add(bid)
            db.session.commit()
            return json.dumps({"success": True, "data": bid.serialize()}), 201
        else:
            return json.dumps({"success": False, "error": "Product not found..."}), 404
    else:
        return json.dumps({"success": False, "error": "Invalid POST request"}), 500

if __name__ == '__main__':
    app.run(host=CLIENT_HOST, port=PORT, debug=True)
