#class variables or static variables
# class Test:
#     name = "shubham"
#     age = 23
#
# print(Test.name)
# print(Test.age)
from os import access



# we can access the class variables inside the method
class Mobile:
    x = 100
    y = 300



    def access_variable(self):
        print(Mobile.x)
        print(Mobile.y)

s1 = Mobile()
s1.access_variable()

# variables that are object specific called instance variable
# we can declare instance variable inside the constructor best way

class Shubham:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def set_mark(self,mark):
        self.mark = mark #decare the instance variable inside the method

    def show(self):
        print(self.name,self.age,self.mark)


t = Shubham("Hanumant",23)
t.set_mark(200)
t.show()


#class variables
class Product:
    product = "laptop"
    price = 45000

print(Product.product)
print(Product.price)

ref1 = Product()
print(ref1.product)
print(ref1.price)

ref2 = Product()
ref3 = Product()
print(ref2.product)
print(ref3.product)

#instance variable
class Laptop:
    def __init__(self,name,sirname):
        self.name = name
        self.sirname = sirname

    def show(self,x):
        self.x= x

ref4 = Laptop("Hanumant","Narwade")
print(ref4.name,ref4.sirname)
ref5 = Laptop("Shubham","Jangilwad")
ref6 = Laptop("Shantanu","Shinde")
print(ref5.name,ref5.sirname)
print(ref6.name,ref6.sirname)
ref5.name = "Arjun"
ref5.sirname = "Jangilwad"
print(ref5.name,ref5.sirname)

# class variable and instance variable
class Remote:
    x = 10
    def __init__(self,y):
        self.y = y

Remote.x = 30 # value change class variable using class name
print(Remote.x)
ref7 = Remote(20)
print(ref7.y)
ref7.y = 40
print(ref7.y)