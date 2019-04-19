# ## http://davidbpython.com/advanced_python/slides/exercise-02-3.html

mylist = ['Hey', 'there', 'I', 'am', 'amazing!']
mydict = {}

for word in mylist:
    mydict[word] = len(word)

print(mydict)
print('----End of exercise 2.1')

mydict = {}

for word in mylist:
    mydict[word] = len(word)
    print('{} has length {}.'.format(word, mydict[word]))
print('----End of exercise 2.2')

mydict = {}

for word in mylist:
    mydict[word] = len(word)
uin = input('Enter one of the words: ').lower().strip()

if uin in mydict:
    print('The word {} has length of {}.'.format(uin, mydict[uin]))
print('----End of exercise 2.3')

if uin in mydict:
    print('The word {} has length of {}.'.format(uin, mydict[uin]))
else:
    print('{} not one of the words'.format(uin))
print('----End of exercise 2.4')

file = open('revenue.txt')
mydict = {}
next(file)

for line in file:
    line = line.split(',')
    mydict[line[0]] = line[2]

print(mydict)
print('----End of exercise 2.5')

file = open('revenue.txt')
mydict = {}
next(file)

for line in file:
    line = line.rstrip()
    line = line.split(',')
    mydict[line[0]] = line[2]

print(mydict)
print('----End of exercise 2.6')

cities = ['Boston', 'Chicago', 'New York',
          'Boston', 'Chicago', 'Boston']

mydict = {}

for state in cities:
    if state in mydict:
        mydict[state] += 1
    else:
        mydict[state] = 1
print(mydict)
print('----End of exercise 2.7')

file = open('students.txt')

mydict = {}
next(file)

for line in file:
    line = line.split(',')
    if line[3] in mydict:
        mydict[line[3]] += 1
    else:
        mydict[line[3]] = 1

print(mydict)
print('----End of exercise 2.8')

file = open('revenue.txt')
next(file)
mydict = {}

for line in file:
    line = line.split(',')
    if line[1] in mydict:
        mydict[line[1]] += float(line[2])
    else:
        mydict[line[1]] = float(line[2])

print(mydict)
print('----End of exercise 2.9')

mydict = {'c': 0.3, 'b': 7, 'a': 5}

for key in sorted(mydict):
    print('{} => {}'.format(key, mydict[key]))
print('----End of exercise 2.10')

for key in sorted(mydict, key = mydict.get):
    print('{} => {}'.format(key, mydict[key]))
print('----End of exercise 2.11')

for key in sorted(mydict, key = mydict.get, reverse = True):
    print('{} => {}'.format(key, mydict[key]))
print('----End of exercise 2.12')

import sqlite3

conn = sqlite3.connect('session_2.db')
cursor = conn.cursor()

query = cursor.execute('SELECT * FROM revenue')

for line in query:
    print(line)
conn.close()
print('----End of exercise 2.13')

conn = sqlite3.connect('session_2.db')
cursor = conn.cursor()

query = cursor.execute('SELECT * FROM revenue ORDER BY 1')

for line in query:
    print(line)
conn.close()
print('----End of exercise 2.14')

conn = sqlite3.connect('session_2.db')
cursor = conn.cursor()

query = cursor.execute('SELECT * FROM revenue ORDER BY 3 DESC')

for line in query:
    print(line)
conn.close()
print('----End of exercise 2.15')

conn = sqlite3.connect('session_2.db')
cursor = conn.cursor()

query = cursor.execute('SELECT state, sum(cost) as Cost FROM revenue GROUP BY 1')

for line in query:
    print(line)
conn.close()
print('----End of exercise 2.16')

conn = sqlite3.connect('session_2.db')
cursor = conn.cursor()

query = cursor.execute('SELECT state, sum(cost) as Cost FROM revenue GROUP BY 1 ORDER BY 2 DESC')

for line in query:
    print(line)
conn.close()
print('----End of exercise 2.17')

conn = sqlite3.connect('session_2.db')
cursor = conn.cursor()

query = cursor.execute('SELECT state, count(cost) FROM revenue GROUP BY 1')

for line in query:
    print(line)
conn.close()
print('----End of exercise 2.18')

conn = sqlite3.connect('session_2.db')
cursor = conn.cursor()

query = cursor.execute('SELECT * FROM students')

for line in query:
    print(line)
conn.close()
print('----End of exercise 2.19')

conn = sqlite3.connect('session_2.db')
cursor = conn.cursor()

query = cursor.execute('SELECT * FROM student_status')

for line in query:
    print(line)
conn.close()
print('----End of exercise 2.20')

conn = sqlite3.connect('session_2.db')
cursor = conn.cursor()

query = cursor.execute('SELECT s.id, s.state, ss.grad_date, ss.gpa FROM students s LEFT JOIN student_status ss ON s.id = ss.id')

for line in query:
    print(line)
conn.close()
print('----End of exercise 2.21')

conn = sqlite3.connect('session_2.db')
cursor = conn.cursor()

query = cursor.execute('SELECT s.id, s.state, ss.grad_date, ss.gpa FROM student_status ss LEFT JOIN students s ON s.id = ss.id')

for line in query:
    print(line)
conn.close()
print('----End of exercise 2.22')

conn = sqlite3.connect('session_2.db')
cursor = conn.cursor()

query = cursor.execute('SELECT s.id, s.state, ss.grad_date, ss.gpa FROM students s JOIN student_status ss ON s.id = ss.id')

for line in query:
    print(line)
conn.close()
print('----End of exercise 2.23')

import pandas as pd

file = pd.read_csv('revenue.txt')
print(file)
print('----End of exercise 2.24')

query = file.groupby('state').sum()
print(query)
print('----End of exercise 2.25')

file = pd.read_csv('students.txt')

query = file.groupby('state').count()
print(query)
print('----End of exercise 2.26')

query = file.groupby('state')['id'].count()
print(query)
print('----End of exercise 2.27')

file_stu = pd.read_csv('students.txt')
file_sta = pd.read_csv('student_status.txt')

query = pd.merge(file_stu, file_sta, on = 'id')
print(query)
print('----End of exercise 2.28')

query = pd.merge(file_stu, file_sta, on = 'id', how = 'right')
print(query)
print('----End of exercise 2.29')

query = pd.merge(file_stu, file_sta, on = 'id', how = 'outer')
print(query)
print('----End of exercise 2.30')

query = pd.merge(file_stu, file_sta, on = 'id', how = 'inner')
print(query)
print('----End of exercise 2.31')

query = pd.merge(file_stu, file_sta, on = 'id', how = 'inner')
print(query[['id', 'gpa']])
print('----End of exercise 2.32')

query = pd.merge(file_stu, file_sta, on = 'id', how = 'inner')
mod_query = query[['id', 'gpa']]
print(mod_query.sort_values('gpa'))
print('----End of exercise 2.33')

print(mod_query.sort_values('gpa', ascending = False))
