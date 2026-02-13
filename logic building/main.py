import my_module
print(my_module.add(5,5))
print(my_module.sub(5,5))

from my_module import add , sub
print(add(7,8))
print(sub(8,9))

import math
print(math.sqrt(81))
print(math.factorial(6))
print(math.pi)
print(math.pow(2,5))

import random
print(random.randint(1,10))
print(random.choice(["red", "blue", "green", "yellow"]))

import random

numbers = [random.randint(1, 50) for i in range(5)]
print(numbers)

a = ["Shubham","Hanumant","Chagan","Harshal","Rajat"]
print(random.choice(a))
