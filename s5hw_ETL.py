import sqlite3
import json

conn = sqlite3.connect('product_catalog.db')
c = conn.cursor()

c.execute('DROP TABLE products')
c.execute('''CREATE TABLE products(
                id TEXT,
                brand TEXT,
                list_price REAL,
                product_description TEXT,
                product_id TEXT,
                product_name TEXT,
                sale_price REAL
            )''')
conn.commit()

file = open('product.json').read()
data = json.loads(file)

row = '''INSERT INTO products VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}")'''
counter = 0
for product in data:
    ID = product
    brand = data[product]['brand']
    list_price = data[product]['list_price']
    product_description = data[product]['product_description']
    product_id = data[product]['product_id']
    product_name = data[product]['product_name']
    sale_price = data[product]['sale_price']

    stmt = row.format(ID, brand, list_price, product_description, product_id, product_name, sale_price)
    c.execute(stmt)


conn.commit()
conn.close()
