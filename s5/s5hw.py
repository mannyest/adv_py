import sqlite3
import json
import sys
import jinja2

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

prod_id = sys.argv[1]
state = sys.argv[2].upper()

this_product = Product(prod_id)

template_dir = 'templates'
env = jinja2.Environment()
env.loader = jinja2.FileSystemLoader(template_dir)

template = env.get_template('product.html')
completed_page = template.render(product=this_product, state=state)

wfh = open(prod_id + '.html', 'w')
wfh.write(completed_page)
wfh.close()

