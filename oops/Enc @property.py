class Student:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age


    @property
    def show(self):
        return ( self.__name,self.__age)

s = Student("Shubham",23,)
print(s.show)

