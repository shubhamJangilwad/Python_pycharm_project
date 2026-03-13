class Student:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def show(self): # this is instance method (self keyword)
        print( self.name,self.age)

s = Student("shubham",23)
s.show()