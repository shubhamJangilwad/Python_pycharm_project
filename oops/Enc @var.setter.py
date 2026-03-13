class Student:
    def __init__(self,salary):
        self.__salary = salary


    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,salary):
        if self.__salary < 25000:
            self.__salary = salary



s = Student(23000)
print(s.salary)
s.salary = 25000
print(s.salary)
