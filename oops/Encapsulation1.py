class BankAccount:
    def __init__(self,balance):
        self.__balance = balance


    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self,amount):
        if amount < self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

B = BankAccount(10000)
B.deposit(1000)
print(B.get_balance())
B.withdraw(5000)
print(B.get_balance())


class StudentMarks:
    def __init__(self,marks):
        self.__marks = marks

    def set_marks(self,mark):
        if mark > 0:
            self.__marks = mark

    def get_marks(self):
        return self.__marks

s = StudentMarks(40)
s.set_marks(70)
print(s.get_marks())
