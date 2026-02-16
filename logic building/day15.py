# even number
a = [2, 5, 7, 8, 10, 13, 16]
b = [i for i in a if i%2== 0]
print(b)

# count vowels
c = input("Enter a string : ")
d = "aeiouAeiou"
count = 0
for i in c:
    if i in d:
        count += 1

print(count)

# sum of integers
data = [10, "20", 30, "hello", 40.5, True, 5]
add = 0
for i in data:
    if type(i) == int and type(i) != bool:
        add +=i
print(add)


# count of chars
s = input("Enter a string: ")
t = {}
for i in s:
    if i  in t:
        t[i] += 1
    else:
        t[i] = 1

for i,k in t.items():
    print(i,k)

# div by 11 and not div by 22
a = [11, 22, 33, 44, 55, 66, 77]
result = list(filter(lambda x :  x%11==0 and  x % 22 != 0 ,a))
print(result)


# rev numbers
a = 1234
rev = 0
while a > 0:
    mod = a % 10
    rev = rev * 10 + mod
    a = a//10

print(rev)

# oop
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def deposite(self,amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

b = BankAccount(10000)
print(b.get_balance())
b.deposite(10000)
print(b.get_balance())
b.withdraw(5000)
print(b.get_balance())
