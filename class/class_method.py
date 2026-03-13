class Student:
    y = "shubham"

    @classmethod # decorator for declare the class method
    def show(cls):
        print(cls.y)

Student.show()