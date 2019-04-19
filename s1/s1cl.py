
var = ['1', '2', '3']                                          ##list object assigned to var
var2 = var                                                     ##var2 assigned value of var
##var2's assignment of var means that now both variables are pointing to the same object in memory NOT that there are two copies of the same object

var.append('4')
print(var2)
##appending to to var changes the object in memory and therefore var2 as well
var = 5
print(var2)
##assigning another object to var means that it is now pointing to a new object in memory, var2 remains pointed at the object it was assigned

#x = [1, 2, 3, 'a', 'b']
#print(dir(x))                                                ##function dir will return all attributes and modules for that data type


import csv

rev_csv = '/users/pipedriveloaner/desktop/Py/advpy/s1/revenue.csv'

total = 0.0
file = open(rev_csv)                                          ##second argument ('rU') refers to opening up file in universal newline mode
csv_reader = csv.reader(file)                                 ##method of module 'csv' that handles the splitting of columns in csv file
next(csv_reader)                                              ##function next() called on a file will remove the first row (headers)
for item in csv_reader:
    price = item[2]
    total += float(price)

print('Sum of prices in revenue.csv: {}'.format(total))

''' SQL LITE 3
while in terminal
> run sqlite3       while in directory
> run .open x       where x is name of files                  ##opens db file
> run .mode x       where x is name of mode                   ##modes include(csv, html, column, list, tabs...)
> run .headers on                                             ##organizes returned items in columns
> run .tables                                                 ##returns list of tables in db
> run .schema x     where x is a table                        ##returns a description of the table (columns and their type)
> run query (eg. SELECT * FROM ...)
> run .quit to exit sqlite
'''


import sqlite3
conn = sqlite3.connect('session_1.db')                        ##Establishing a connection with database
c = conn.cursor()                                             ##Cursor object is necessary for executing/working with the database

rs = c.execute('SELECT * FROM revenue')                       ##Executing query

total = 0.0
for items in rs:
    price = items[-1]
    total += price
print('Total or sum of all prices: {}'.format(total))

rs = c.execute('SELECT * FROM revenue')
price_list = []
for items in rs:
    price = items[-1]
    price_list.append(price)
print('List of Prices via SQL: {}'.format(price_list))

num_prices = len(price_list)
sum_prices = (sum(price_list))
sort_prices = (sorted(price_list))

avg_price = sum_prices / num_prices
print('Average price: {}\n'.format(avg_price))

conn.close()                                                  ##close the connection with the databse that was opened


import pandas as pd                                           ##anaconda documentation or pandas module required

rev_file = 'revenue.csv'
rev_read = pd.read_csv(rev_file)
print(rev_read)
## pandas library/module allows for printing of files in an organized(spreadsheet) like manner
