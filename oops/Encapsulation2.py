class Room:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self,new_balance):
        self.__balance = new_balance

r = Room("shubham",23000)
print(r.name)
print(r.get_balance())
r.set_balance(25000)
print(r.get_balance())
