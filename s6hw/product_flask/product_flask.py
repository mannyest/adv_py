#!/usr/bin/env python

import flask
import sqlite3
import json
import jinja2
import os

app = flask.Flask(__name__)

BASE_DIR = '/Users/pipedriveloaner/Desktop/Py/advpy/s6/s6hw/product_flask'
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

class Product:
    '''represents one object in the products_catalog database and can be displayed in a product catalog online'''

    @staticmethod
    def get_data(p_id):
        conn = sqlite3.connect('product_catalog.db')
        c = conn.cursor()

        product = c.execute(''' SELECT * FROM products
                                WHERE id = '{}'
                                ; '''.format(p_id))

        return c.fetchone()

    def __init__(self, p_id):

        ID, brand, list_price, product_description, product_id, product_name, sale_price = Product.get_data(p_id)
        self.ID = ID
        self.brand = brand
        self.list_price = list_price
        self.description = product_description
        self.id = product_id
        self.name = product_name
        self.sale_price = sale_price

    def __str__(self):
        return 'id={}, brand={}, sale_price={}'.format(self.id, self.brand, self.sale_price)

    def get_tax(self, state):

        tax_file = open('state_tax.json').read()
        tax_rates = json.loads(tax_file)

        return tax_rates[state]

    def get_savings_pct(self):
        return self.list_price - self.sale_price


@app.route('/pview')
def view_product():
    print('*** DEBUG:  inside view_product() ***')
    prod_id = flask.request.args.get('prod_id')
    state = flask.request.args.get('state')

    img_path = 'images/{}.jpg'.format(prod_id)

    product = Product(prod_id)

    completed_page = flask.render_template('view_product.html', product=product, state=state, image_path=img_path)

    prod_temp = os.path.join(TEMPLATES_DIR, prod_id + '.html')

    wfh = open(prod_temp, 'w')
    wfh.write(completed_page)
    wfh.close()

    return flask.render_template('{}.html'.format(prod_id))

@app.route('/plist')
def list_products():
    print('*** DEBUG:  inside list_product() ***')
    conn = sqlite3.connect('product_catalog.db')
    c = conn.cursor()

    query_products = c.execute('''SELECT id FROM products ;''')
    p_list = []

    for item in query_products:
        item = item[0]
        p_item = Product(item)
        p_list.append(p_item)

    return flask.render_template('list_products.html', product_list=p_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
