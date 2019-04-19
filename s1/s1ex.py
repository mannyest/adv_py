##Exercises Session 1 - AdvPy by Blaikie uh - 6th June 2018 - http://davidbpython.com/advanced_python/slides/exercise-01-3.html

csv_file = open('revenue.csv')
for line in csv_file:
    print(line)
print('End of Exercise 1.1')

csv_file = open('revenue.csv')
counter = 0
for line in csv_file:
    counter += 1
    print(line)
print(counter)
print('End of Exercise 1.2')

csv_file = open('revenue.csv')
counter = 0
for line in csv_file:
    counter += 1
    print(counter, line)
print(counter)
print('End of Exercise 1.3')

csv_file = open('revenue.csv')
counter = 0
for line in csv_file:
    counter += 1
    line = line.rstrip()
    print(counter, line)
print(counter)
print('End of Exercise 1.4')

csv_file = open('revenue.csv')
for line in csv_file:
    line = line.rstrip()
    line = line.split(',')
    print(line)
print('End of Exercise 1.5')

csv_file = open('revenue.csv')
next(csv_file)
for line in csv_file:
    line = line.rstrip()
    line = line.split(',')
    print(line[2])
print('End of Exercise 1.6')

csv_file = open('revenue.csv')
next(csv_file)
for line in csv_file:
    line = line.rstrip()
    line = line.split(',')
    print(line[2], float(line[2]) * 2)
print('End of Exercise 1.7')

csv_file = open('revenue.csv')
next(csv_file)
total = 0.0
for line in csv_file:
    line = line.rstrip()
    line = line.split(',')
    total += float(line[2])
print(total)
print('End of Exercise 1.8')

csv_file = open('revenue.csv')
next(csv_file)
prices = []
for line in csv_file:
    line = line.rstrip()
    line = line.split(',')
    prices.append(float(line[2]))
print(prices)
print('End of Exercise 1.9')

values = [1, 3, 4, 10, 15]
if len(values) % 2 != 0:
    median = values[int(len(values) / 2)]
else:
    l_half = values[int((len(values) / 2) - 1)]
    h_half = values[int((len(values) / 2))]
    median = (l_half + h_half) / 2
print(median)
print('End of Exercise 1.10')

values = [3, 1, 10, 15, 4]
values = sorted(values)
if len(values) % 2 != 0:
    median = values[int(len(values) / 2)]
else:
    l_half = values[int((len(values) / 2) - 1)]
    h_half = values[int((len(values) / 2))]
    median = (l_half + h_half) / 2
print(median)
print('End of Exercise 1.11')

values = [6, 1, 3, 2, 4, 5]
values = sorted(values)
if len(values) % 2 != 0:
    median = values[int(len(values) / 2)]
else:
    l_half = values[int((len(values) / 2) - 1)]
    h_half = values[int((len(values) / 2))]
    median = (l_half + h_half) / 2
print(median)
print('End of Exercise 1.12')

import csv

file = open('revenue.csv')
csv_read = csv.reader(file)
for line in csv_read:
    print(line)
print('End of Exercise 1.13')

prices = 0.0
file = open('revenue.csv')
csv_read = csv.reader(file)
next(csv_read)
for line in csv_read:
    prices += float(line[2])
print(prices)
print('End of Exercise 1.14')

prices = []
counter = 0
file = open('revenue.csv')
csv_read = csv.reader(file)
next(csv_read)
for line in csv_read:
    prices.append(float(line[2]))
    counter += 1
print('Count: {}'.format(counter))
print('Sum: {}'.format(sum(prices)))
print('Max: {}'.format(max(prices)))
print('Min: {}'.format(min(prices)))
print('End of Exercise 1.15')

print('''*In Terminal*
> sqlite3
> .open session_1.db
> .tables
> .schema revenue
> .mode column
> .headers on
> select * from revenue;
> select price from revenue;''')
print('End of Exercise 1.16 - 1.20')

import sqlite3

conn = sqlite3.connect('session_1.db')
c = conn.cursor()

query1 = c.execute('select * from revenue')
for row in query1:
    print(row)
print('End of Exercise 1.21')

query2 = c.execute('select * from revenue')
for row in query2:
    print(row[2])
print('End of Exercise 1.22')

import pandas as pd

file = pd.read_excel('revenue.xls')
print(file)
print('End of Exercise 1.23')

file = pd.read_excel('revenue.xls')
print(file['price'])
print('End of Exercise 1.24')

p_count = len(file['price'])
p_sum = sum(file['price'])
p_avg = p_sum / p_count
p_sort = sorted(file['price'])
if len(p_sort) % 2 != 0:
    p_median = p_sort[int(len(values) / 2)]
else:
    l_half = p_sort[int((len(values) / 2) - 1)]
    h_half = p_sort[int((len(values) / 2))]
    p_median = (l_half + h_half) / 2

print(p_count)
print(p_sum)
print(p_avg)
print(p_median)
print('End of Exercise 1.25')
