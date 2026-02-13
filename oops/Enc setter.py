class S:
    def __init__(self,salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self,add):
        self.__salary = add

ref = S(0)
ref.set_salary(20000)
print(ref.get_salary())
