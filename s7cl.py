

##encapsulation : the object's data will remain 'uncorrupted'
##inheritance: ability for one class to inherit from another class
##polymorphism: two objectes that support the same method and do different things when called

class Incrementer:
    def __init__(self, val):
        self.innerval = val
    def increment(self):
        self.innerval = self.innerval + 1
    def __str__(self):
        return str(self.innerval)

x = Incrementer(5)
x.increment()
x.increment()
print(x)
## this class is poorly designed because it can be initialized or called with any data type (int, string, fload, list etc.) but the functions really are meant for it to be an int (hence the increment funcion)

'---------------------------'

class Incrementer:
    def __init__(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError('Object must be integer or float.')
        ##raises the typeerror if you try to initialize an object object with anything but int or fload
        self.innerval = val
    def increment(self):
        self.innerval = self.innerval + 1
    def __str__(self):
        return str(self.innerval)

# y = Incrementer('hello')  would raise a type error

class GetSet(object):

    def __init__(self,value):
        self.attrval = value

    @property
    def var(self):
        print('thanks for calling me -- returning {}'.format(self.attrval))
        return self.attrval

    @var.setter
    def var(self, value):
        print("thanks for setting me -- setting 'var' to {}".format(value))
        self.attrval = value

    @var.deleter
    def var(self):
        print('should I thank you for deleting me?')
        del self.attrval
''' this class has three functions of the same name 'var', generally each var function will replace the other in a top down fashion but in this case each have been decorated. When a function is decorated with
@property will be called automagically the object "attribute" is printed
@var.setter will be called automagically the object "attribute" is set ( = )
@var.deleter will be called automagically the object "attribute" is called with del '''

'---------------------------'

from bs4 import BeautifulSoup
import requests

ticker = 'NFLX'

response = requests.get('https://www.marketwatch.com/investing/stock/{}'.format(ticker))

soup = BeautifulSoup(response.text, 'html.parser')


nflx_price = soup.find_all('bg-quote', {'class': 'value'})
for line in nflx_price:
  print(line.text)

'---------------------------'

import re

x = 'q'

if re.search(r'q', x):                   ##re.search takes 2 arguments (pattern and ...
    print("match found!")
else:
    print("no match.")

y = 'quit'

if re.search(r'q', y):
    print("match found!")
else:
    print("no match.")

y = 'something with many qqqs in it'

if re.search(r'q', y):
    print("match found!")
else:
    print("no match.")
