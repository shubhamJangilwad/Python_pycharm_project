# class Car:
#     brand = "maruti suzuki"
#     price = 120000
#
# c1 = Car()
# print(c1.brand)
# print(c1.price)

class Book:
    def __init__(self,title,price):
        self.title = title
        self.price = price
c1 = Book("itshalla",30000)
c2 = Book("school",25000)
print(c1.title , c1.price)
print(c2.title, c2.price)

class Employee:
    def __init__(self):
        self.company = "Tcs"
        self.salary = 30000
c1 = Employee()
c2 = Employee()
print(c1.company,c2.salary)
print(c2.company,c2.salary)





class Student:
    def __init__(self, name):
        self.name = name

    def show_name(self):     # instance method
        print(self.name)

s1 = Student("Ram")
s1.show_name()
print(s1.name)
