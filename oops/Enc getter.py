class Student:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    #use get method
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

ref = Student("Shubham",23)
print(ref.get_name())
print(ref.get_age())
