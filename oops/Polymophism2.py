# class Student:
#     def __init__(self,marks):
#         self.marks = marks
#
#     def __add__(self, other):
#         return self.marks + other.marks
#
# s1 = Student(50)
# s2 = Student(70)
#
# print(s1 + s2)

# method overloading
class Calculator:
    def sum(self,a,b,c=0):
        return a+b+c

ref = Calculator()
print(ref.sum(10,20))
print(ref.sum(10,20,30))