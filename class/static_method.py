#not an object specific
#not a class specific
class Student:
    x = "Hanumant"

    @staticmethod #decorator for declare static method
    def show():
        print(Student.x)

Student.show()