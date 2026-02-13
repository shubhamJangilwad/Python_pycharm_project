class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print("name: ",self.name)
        print("Age: ",self.age)

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def teach(self):
        print("Teaching",self.subject)

class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name, age)
        self.grade = grade
    def study(self):
        print("Studying in grade ",self.grade)

t = Teacher("shubham",23,"Math")
s = Student("shubham",23,"A")
t.display_info()
t.teach()
s.display_info()
s.study()


