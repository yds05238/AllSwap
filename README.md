All Swap Backend (and Frontend)

Step 1: Fork or Download the project codes from this repository

Step 2: Inside the folder for the project, run this code: pip install -r requirements.txt

Step 3: Once the downloading stops, run python main.py

Step 4: the Flask app is located at http://localhost:5000/



## AllSwap Online Buy/Sell Platform:
* Spark Design Project Team

## AllSwap Website contains:
* User register 
* User login
* User logout 
* Change password
* Reset password
* Add Products to Cart
* Posting Products for Sale
* Organize Products by Category

## Usage :
### Run project by :

``` python

# Clone this repository. Inside the local directory, run the following commands

1. pip install -r requirements.txt

2. python main.py 

```

That's it. I think... 

## Done :

Now the project is running at `http://localhost:5000` and your routes is:


| Route                                                      | HTTP Method 	   | Description                           	      |
|:-----------------------------------------------------------|:----------------|:---------------------------------------------|
| {host}       	                                             | GET       	     | Home page                                    |
| {host}/add                                                 | POST     	     | Contact us message                           |
| {host}/addItem .                                           | POST     	     | Search products by price range               |
| {host}/products/{id}                                       | POST     	     | All products page                            |
| {host}/remove .                                            | GET      	     | Forget password page                         |
| {host}/removeItem                                          | POST     	     | Send reset password e-mail                   |
| {host}/displayCategory                                     | POST     	     | Enter new password                           |
| {host}/account/profile                                     | POST     	     | User register                                |
| {host}/account/profile/edit                                | POST     	     | User login                                   |
| {host}/account/orders                                      | GET     	       | User logout                                  |
| {host}/account/profile/changePassword                      | GET     	       | User profile                                 |
| {host}/updateProfile                                       | POST     	     | Change user profile image                    |
| {host}/loginForm                                           | POST     	     | User change password                         |
| {host}/login                                               | POST     	     | Add order to cart                            |
| {host}/                | POST     	     | Add order to cart from slider                |
| {host}/increase_cart_product_quantity/{id}                 | POST     	     | Increase order quantity                      |
| {host}/edit_cart_product_quantity/{id}                     | POST     	     | Enter order quantity                         |
| {host}/decrease_cart_product_quantity/{id}                 | POST     	     | Decrease order quantity                      |
| {host}/delete_product_from_cart/{id}                       | POST     	     | Delete order                                 |
| {host}/add_to_cart                                         | POST   	       | Cart                                         |
| {host}/buy                                                 | POST     	     | Buy orders                                   |
| {host}/product_review/{id}                                 | POST     	     | Add product review                           |
| {host}/slider_product_review/{id}                          | POST     	     | Add slider product review                    |
| {host}/preview_production/{id}                             | GET     	       | Product detail                               |
| {host}/preview_production_slider/{id}                      | GET     	       | Slider Product detail                        |
| {host}/categories/{category}                               | GET     	       | Search products by category                  |
| {host}/user_search                                         | POST     	     | Search in products name                      |

