import unittest
import json
import requests

# NOTE: Make sure you run 'pip install requests' in your virtualenv

# URL pointing to your local dev host
LOCAL_URL = 'http://localhost:5000'
BODY = {'text': 'Hello, World!', 'username': 'Megan'}
USER = {'email': 'jy392@cornell.edu', 'username': 'jy392', 'rating': 0}
PRODUCT = {'name': "Macbook", "price": 800}
p2 = {'name': 'pencil', 'price': 10}
p3 = {'name': 'textbook', 'price': 300}
p4 = {'name': "An Introduction to Mechanics", 'price': 145}
p5 = {'name': "Probability And Statistics", "price": 199}

class TestRoutes(unittest.TestCase):
    # Tests getting all posts
    def test_get_initial_products(self):
        res = requests.get(LOCAL_URL + '/api/products/')
        assert res.json()['success']
    
    # Tests creating a post
    def test_create_products(self):
        res = requests.post(LOCAL_URL + '/api/products/', data=json.dumps(PRODUCT))
        product = res.json()['data']
        assert res.json()['success']
        assert product['name'] == 'Macbook'
        assert product['price'] == 800
        res2 = requests.post(LOCAL_URL + '/api/products/', data=json.dumps(p4))
        product2 = res2.json()['data']
        assert res2.json()['success']
        assert product2['name'] == "An Introduction to Mechanics"
        assert product2['price'] == 145
        res3 = requests.post(LOCAL_URL + '/api/products/', data=json.dumps(p5))
        product3 = res3.json()['data']
        assert res3.json()['success']
        assert product3['name'] == "Probability And Statistics"
        assert product3['price'] == 199
        
    
    # Tests getting a post by id
    def test_get__product(self):
        res = requests.post(LOCAL_URL + '/api/products/', data=json.dumps(PRODUCT))
        product = res.json()['data']

        res2 = requests.post(LOCAL_URL + '/api/products/', data=json.dumps(p2))
        product2 = res2.json()['data']
        res3 = requests.post(LOCAL_URL + '/api/products/', data=json.dumps(p3))
        product3 = res3.json()['data']
        res4 = requests.post(LOCAL_URL + '/api/products/', data=json.dumps(p4))
        product4 = res4.json()['data']
        res5 = requests.post(LOCAL_URL + '/api/products/', data=json.dumps(p5))
        product5 = res5.json()['data']


        res = requests.get(LOCAL_URL + '/api/product/' + str(product['id']) + '/')
        assert res.json()['data'] == product
        res = requests.get(LOCAL_URL + '/api/product/' + str(product2['id']) + '/')
        assert res.json()['data'] == product2
        res = requests.get(LOCAL_URL + '/api/product/' + str(product3['id']) + '/')
        assert res.json()['data'] == product3
        res = requests.get(LOCAL_URL + '/api/product/' + str(product4['id']) + '/')
        assert res.json()['data'] == product4
        res = requests.get(LOCAL_URL + '/api/product/' + str(product5['id']) + '/')
        assert res.json()['data'] == product5

    # Tests updating a post
    def test_edit_product_price(self):
        res = requests.post(LOCAL_URL + '/api/products/', data=json.dumps(PRODUCT))
        product_id = res.json()['data']['id']
        res = requests.post(LOCAL_URL + '/api/product/' + str(product_id) + '/',
                            data=json.dumps({"price":650}))
        assert res.json()['success']

        res = requests.get(LOCAL_URL + '/api/product/' + str(product_id) + '/')
        assert res.json()['data']['price'] == 650

    # Tests deleting a post
    def test_delete_post(self):
        res = requests.post(LOCAL_URL + '/api/products/', data=json.dumps(PRODUCT))
        product_id = res.json()['data']['id']
        res = requests.delete(LOCAL_URL + '/api/product/' + str(product_id) + '/')
        assert res.json()['success']

    # Tests getting all bids of a post
    def test_get_initial_products(self):
        res = requests.post(LOCAL_URL + '/api/products/', data=json.dumps(PRODUCT))
        product_id = res.json()['data']["id"]
      
        res1 = requests.get(LOCAL_URL + '/api/product/' + str(product_id) + '/bids/')
        assert res1.json()['success']

    # Tests creating bid 
    def test_create_bid(self):
        res = requests.post(LOCAL_URL + '/api/products/', data=json.dumps(PRODUCT))
        product_id = res.json()['data']['id']
        bid = {'amount': 750, 'product_id': product_id}
        res = requests.post(LOCAL_URL + '/api/product/' + str(product_id) + '/bid/',
                            data=json.dumps(bid))
        assert res.json()['success']

        res = requests.get(LOCAL_URL + '/api/product/' + str(product_id) + '/bids/')
        assert res.json()['success']
        bids = res.json()['data']
        assert len(bids) == 1
        assert bids[0]['amount'] == 750

        res = requests.delete(LOCAL_URL + '/api/product/' + str(product_id) + '/')
        assert res.json()['success']

    # Tests getting a post that doesn't exist
    def test_get_invalid_post(self):
        res = requests.get(LOCAL_URL + '/api/product/1000/')
        assert not res.json()['success']

    # Tests editing a post that doesn't exist
    def test_edit_invalid_post(self):
        res = requests.post(LOCAL_URL + '/api/product/1000/',
                            data=json.dumps({'price': 10}))
        assert not res.json()['success']

    # Tests deleting a post that doesn't exist
    def test_delete_invalid_post(self):
        res = requests.delete(LOCAL_URL + '/api/product/1000/')
        assert not res.json()['success']

    # Tests getting the comments from a post that doesn't exist
    def test_get_comments_invalid_post(self):
        res = requests.get(LOCAL_URL + '/api/product/1000/bids/')
        assert not res.json()['success']

    # Tests posting a comment to a post that doesn't exist
    def test_post_invalid_comment(self):
        res = requests.post(LOCAL_URL + '/api/products/', data=json.dumps(PRODUCT))
        product_id = res.json()['data']['id']
        bid = {'amount': 750, 'product_id': product_id}
        res = requests.post(LOCAL_URL + '/api/product/1000/bid/', data=json.dumps(bid))
        assert not res.json()['success']

    # Tests to make sure that the post id increments
    def test_post_id_increments(self):
        res = requests.post(LOCAL_URL + '/api/products/', data=json.dumps(PRODUCT))
        product_id = res.json()['data']['id']

        res2 = requests.post(LOCAL_URL + '/api/products/', data=json.dumps(PRODUCT))
        product_id2 = res2.json()['data']['id']

        assert product_id + 1 == product_id2

if __name__ == '__main__':
    unittest.main()