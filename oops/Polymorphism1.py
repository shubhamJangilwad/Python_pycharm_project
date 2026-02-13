#Method overriding - same method name but different behaviour
class A:
    def show(self):
        print("Morning")

class B:
    def show(self):
        print("Hii")


a = A()
b = B()
b.show()
a.show()