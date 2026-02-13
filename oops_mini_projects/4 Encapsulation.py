class Wallet:
    def __init__(self,balance):
        self.__balance = balance
        self.__transaction = 0


    def add_money(self,amount):
        if amount > 0:
            self.__balance += amount
            self.__transaction +=1
            print("added money")

        else:
            print("money not added")


    def spend_money(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.__transaction +=1
            print("spend money")

        else:
            print("not spend")

    def get_balance(self):
        return self.__balance

    def transaction_summary(self):
        print("total transactions",self.__transaction)



w = Wallet(1000)
w.add_money(500)
w.spend_money(1000)
print(w.get_balance())
w.transaction_summary()