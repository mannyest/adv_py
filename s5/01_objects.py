lines = [ 'id:fname:lname:address:city:state:zip',
          'jk43:John:Kane:23 Marfield Lane:Plainview:NY:10024' ]

class Student:

    @staticmethod
    def marshall_data(student_id):
        line = lines[1]
        items = line.split(':')
        if items[0] == 'jk43':
            return items

    def __init__(self, stu_id):
        ( line_id, fname, lname, 
          address, city, state, stu_zip) = Student.marshall_data(stu_id)
        self.id = stu_id
        self.fname = fname
        self.lname = lname
        self.address = address
        self.city = city
        self.state = state
        self.zip = stu_zip

    def get_full_name(self):
        """ returns 'firstname lastname' in a single string """
        return('{} {}'.format(self.fname, self.lname))

stu = Student('jk43')

#print(stu.fname, stu.lname)   # John Kane
print(stu.get_full_name())

