class Bankaccount:
    def __init__(self,name,bank_account_no,balance,pin):
        self.name = name
        self.bank_account_no = bank_account_no
        self.__balance = balance
        self.__pin = pin

    def check_balance(self):
        return self.__balance

    def withdraw_money(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("please collect your cash")
        else:
            print("ammount is not sufficiant")

    def deposit_money(self,amount):
        if amount > 0:
            self.__balance += amount
            print("money added to the account")
        else:
            print("money not added to the account")

    def change_pin(self,new_pin):
        self.__pin = new_pin

    def get_balance(self):
        return self.__balance

    def get_new_pin(self):
        return self.__pin


b = Bankaccount("shubham",101,10000,431602)

print("First checking the account Balance :",b.get_balance())
b.deposit_money(5000)
print("check balance after deposit :",b.get_balance())
b.withdraw_money(5000)
print("check balance after withdraw :",b.get_balance())
b.change_pin(880523)
print("set new pin :",b.get_new_pin())



