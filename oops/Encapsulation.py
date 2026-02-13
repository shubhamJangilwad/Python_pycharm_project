from tkinter.font import names


class Student:
    def __init__(self,name,age):#constructor
        self.__name = name #private variable
        self.__age = age   #private variable

#Acessesing the private variable using public getter and setter
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self,name):
        self.__name = name

    def set_age(self,age):
        self.__age = age

s = Student("shubham",23)
print(s.get_name())
print(s.get_age())

s.set_name("Hanumant")
s.set_age(22)


print(s.get_name())
print(s.get_age())



