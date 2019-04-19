


class Car:

	def __init__(self, model, color = None):				## __init__ is short for initializer, as it is required in order to 'initialize' an object and give it it's own attributes (parameters of init)

		self.model = model
		self.color = color

	def get_color(self):
		return (self.color)

## __init__ is one example of a 'private' or inherent function, denoted by the double underscores before and after the name
## self refers to the object itself and is required as all functions within the calss will are to be applied to the object

bmw = Car('325i')											##creating an object using the class 'automagically' calls the init function
tesla = Car('Model 3', 'Red')

# print(bmw.model, bmw.color)
# print(tesla.model, tesla.color)
#
#
# tesla_color = tesla.get_color()
# print(tesla_color)
#
# print(tesla.__dict__)


class Student:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @staticmethod                                           ##@staticmethod is a decorator that allows the function below it to not take the object as an argument
    def gpa_grade(gpa):
        if gpa == 3.8:
            return ('A-')

    def set_gpa(self, floatval):
        self.gpa = floatval

    def get_grade(self):
        return self.gpa_grade(self.gpa)                     ##since gpa_grade function was defined without 'self' (decorated) then it will shown as undefined unless called as self.gpa_grade



chico = Student('Chico', 'Swav')                            ##creating object
chico.set_gpa(3.8)                                          ##calling function set_gpa and given an argument
print(chico.get_grade())                                    ##calls to print the returned value of function



''' part 2 '''


class Student:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        self.stuid = 8
        self.street = 'Park'
        self.city = 'New York'
        self.state = 'NY'
        self.zip = 10031


file =  open('student.html')
text = file.read()

print(text)

guy = Student('Potz', 'Cabayza')                        ##create student object with first and last name
##this object inherets all other attributes from the __init__ function (stuid, street, state etc.)
page = text.format(obj=guy)

wfile = open('wstudent.html', 'w')
wfile.write(page)
wfile.close()

print('testing')
