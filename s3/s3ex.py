##http://davidbpython.com/advanced_python/slides/exercise-03-3.html

import datetime

indpndnc = datetime.date(2018, 7, 4)
print(indpndnc, type(indpndnc))
##datetime.date(y, m, d) returns a date object with the provided year, month, day arguments
print('---- End of Exercise 3.1 ----')

today = datetime.date.today()
print(today, type(today))
##datetime.date.today() returns a date object for current date
print('---- End of Exercise 3.2 ----')

dobj = str(datetime.date(1941, 12, 7))
print(dobj, type(dobj))
print('---- End of Exercise 3.3 ----')

dobj = datetime.date(1969, 7, 20)
fdobj = dobj.strftime('%m/%d/%y')
print(fdobj, type(fdobj))
##date-object.strftime('%m/%d/%y') converts a date object into string type
print('---- End of Exercise 3.4 ----')

datestr = '1944-06-06'
dobj = datetime.datetime.strptime(datestr, '%Y-%m-%d')                      ##datetime.datetime.strptime(string, format)
fdobj = dobj.date()                                                         ##datetime-object.date() converts to a datetime object to date object
print(fdobj, type(fdobj))
##converting a string date into datetime object type and then date object type
print('---- End of Exercise 3.5 ----')

import mannyhi                                                              ##imported module from personal package that was intalled in sys.path

x = mannyhi.greet()
print(x)
## calling module function
print('---- End of Exercise 3.6 ----')

y = mannyhi.greet('blakie uh')
print(y)
print('---- End of Exercise 3.7 ----')

def increment(val):
    ival = val + 1
    return ival
print('''created a test file test_increment.py with three test functions''')
print('---- End of Exercise 3.8 ----')

print(''' added both assertions to test_increment_int() from test_increment.py''')
print('---- End of Exercise 3.9 ----')


print(''' added both assertions to test_increment_float() from test_increment.py''')
print('---- End of Exercise 3.10 ----')

print(''' added assertion to test_increment_str() from test_increment.py''')
print('---- End of Exercise 3.11 ----')

print('''created github account, followed guide on commiting and uploaded personal package. Direct URL https://github.com/mannyest/mannyhi/tree/master/mannyhi''')
print('---- End of Exercise 3.12 - 3.14 ----')
