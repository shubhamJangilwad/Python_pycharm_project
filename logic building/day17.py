import threading
import time

def prepare(order):
    print("Preparing", order)
    time.sleep(3)      # cooking time
    print(order, "ready")

start = time.time()

t1 = threading.Thread(target=prepare, args=("Pizza",))
t2 = threading.Thread(target=prepare, args=("Burger",))
t3 = threading.Thread(target=prepare, args=("Pasta",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Total time:", round(time.time()-start,2))

import math

a = 1234
rev = 0
while a > 0:
    num = a % 10
    rev = rev * 10 + num
    a = a // 10

print(rev)

import  threading

def bg():
    for i in range(10):
        print("Current Thread",threading.current_thread().name)

t = threading.Thread(target=bg)
t.start()
t.join()
print("Main Thread")

import threading

lock = threading.RLock()

def task():
    lock.acquire()
    print("First lock acquired")

    lock.acquire()   # same thread trying again → DEADLOCK
    print("Second lock acquired")

    lock.release()
    lock.release()

t = threading.Thread(target=task)
t.start()
t.join()

data = [1,2,2,3,4,4,5,1,6]
tata = []
for i in data:
    if i not in tata:
        tata.append(i)
print(tata)


# max len of word
data = "Python makes programming very powerful and simple"
b = (data.split())
a = 0
c = ''
for i in b:
    if len(i) > a:
        a = len(i)
        c = i
print(c)

a = 10
b = 20
a,b = b,a
print(a)
print(b)

uppercase = 0
lowercase = 0
digit = 0
special = 0
s  = "PyTh0n@2026"
for i in s:
    if i.isupper():
        uppercase += 1
    elif i.islower():
        lowercase += 1
    elif i.isdigit():
        digit += 1
    else:
        special += 1

print("uppercase: ",uppercase)
print("lowercase: ",lowercase)
print("digits: ",digit)
print("special: ",special)

from math import pow
print(math.pow(2,5))
print(math.pow(3,3))




# need correction
class Person:
    def __init__(self,name,age , salary):
        self.name = name
        self.age = age
        self.salary = salary

    def show_details(self):
        return self.name,self.age,self.salary

p = Person("shubham",23,20000)
print("Name:",p.name)
print("Age:",p.age)
print("Salary:",p.salary)



# prime numbers
n = int(input("Enter a number: "))
count = 0
for i in range(1,n+1//2):
    if n % 1 == 0:
        count += 1
if count == 1:
    print("Prime")
else:
    print("Not Prime")























