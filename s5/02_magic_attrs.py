

class CustomInt:
    '''this is a doc string'''
    def __init__(self, val=0):
        self.inner_val = val

    def increment(self):
        self.inner_val = self.inner_val + 1

    def __str__(self):
        return str(self.inner_val)
    ##is called automatically when the object is printed

    def __add__(self, val):
        self.inner_val += val
        return self
    ##is called automatically when the object is called with the '+' opperator

#    def __len__(self):
#        strval = str(self.inner_val)
#        return len(strval)

#    def addval(self, otherval):
#        self.inner_val = self.inner_val + otherval

#    def __add__(self, otherval):
#        self.inner_val = self.inner_val + 1

x = CustomInt()
print(x + 5)                            ##possible to use '+' becuase of the __add__ function

print(x.__doc__)
