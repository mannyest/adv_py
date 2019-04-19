'''
One time operation
Take the data in JSON file and
insert into a datatable

Build the page
pull the data from a datasbase
populate a Product oject
insert the data into a jinja2 template

save the completed page
'''


myd = {  'A1':  { 'fname': 'Joe',   'lname': 'Wilson', 'balance': 23.9 },
         'A2':  { 'fname': 'Marcy', 'lname': 'Post',   'balance': 303.21 },
         'A3':  { 'fname': 'Gwen',  'lname': 'Arvez',  'balance': 179.30 }  }

py_stmt = "{} {}:  {}"

for key in myd:
    row_dict = myd[key]
    print(key, row_dict)

import sqlite3

create_table = "CREATE TABLE ledger (fname TEXT, lname TEXT, balance FLOAT)"

sql_stmt = "INSERT INTO ledger VALUES '{}', '{}', {}"          # INSERT INTO ledger VALUES ('Joe', 'Wilson', 23.9)

conn = sqlite3.connect('that.db')
c = conn.cusrsor()

for key in :
    row_dict = myd[key]
    fname, lname, bal = row_dict['fname'], row_dict['lname'], row_dict['balance']
    output = sql_stmt.format(fname, lname, bal)
    cursor.execute(stmt)

conn.commit()