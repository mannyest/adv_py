##in-class session by blaikie uh 2018.06.12
'''
x = { 'a': [1, 2, 3],
      'b': [4, 5, 6]  }


for key in x:
    print('key: {} and sum of values: {}'.format(key, sum(x[key])))         ##q1
    print('last item of each key are: {}'.format(x[key][-1]))               ##q2
    x[key].append(10)                                                       ##q3

count = 0
for key in x:
    if count == 0:
        print('first item in first key: {}'.format(x[key][0]))
    else:
        print('second item in second key: {}'.format(x[key][1]))
    count += 1

var1 = ['a', 'b']

var2 = ','.join(var1)
print(var1, var2)
'''

import pandas as pd

# revs = pd.read_csv('/Users/pipedriveloaner/Desktop/Py/AdvPy_Blaikie/S2/session_2_working_files/inclass/revenue.txt')
# #print(revs)

# pd1 = revs.groupby('state').sum()
# print(pd1)

# srevs = revs[['state', 'cost']]
# pd2 = srevs.groupby('state').sum()
# print(pd2)

students = pd.read_csv('/Users/pipedriveloaner/Desktop/Py/advpy/s2/students.txt')
status = pd.read_csv('/Users/pipedriveloaner/Desktop/Py/advpy/s2/student_status.txt')

sjoin =  students.merge(status, on = 'id')
print(sjoin)
