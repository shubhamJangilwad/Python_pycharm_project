def show():
    print("Welcom to Python")
show()

def positive(a):
    if a > 0:
        print("positive")
    else:
        print("negative")
positive(8)

def add(a,b):
    return a+b
x = add(2,3)
print(x)


def even_odd(a):
    if a % 2 == 0:
        return True
    else:
        return False

x = even_odd(8)
print(x)

from functools import reduce
y = int(input("Enter a number: "))
z = []
for i in range(1,y+1):
    z.append(i)
x = reduce(lambda a,b:a*b,z)
print(x)



