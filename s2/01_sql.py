# SQL stub program


import sqlite3
conn = sqlite3.connect('inclass.db')  # a db connection object

c = conn.cursor() 

query = 'SELECT * FROM user'

rs = c.execute(query)

# row = rs.fetchone()    # fetch just one row

for row in rs:           # loop through result set
    print(row)


conn.close()

