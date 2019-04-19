
class IntList(list):

    def append(self, obj):
        list.append(self, obj)


x = IntList([1, 2, 3])

x.append(4)

print(x)


'''The Three pillars of OOP'''

## encapsulation: the 'protection' of data within the object

class IntList:

    def append(self, val):
        if not isinstance(val, int):
            raise TypeError('int please')
    ## in this case we are protecting the value of the val being appened

## inheritance

class Parent:
    def do(self):
        print("I am the parent")

class Child(Parent):
    def greet(self):
        print('hello')

son = Child()

son.greet()
son.do()

## polymorphism: