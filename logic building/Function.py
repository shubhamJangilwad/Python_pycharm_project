# def greet(name):
#     return name
# y = greet("moreshwar")
# print(y)
from os.path import split

# def check_zero(num):
#     if num == 0:
#         return "Zero"
#     else:
#         return "Not zero"
# result = check_zero(8)
# print(result)


# def add(a,b):
#     return a + b
# result = add(4,5)
# print(result)


# def print_char(s):
#     for i in s:
#         print(i)
# print_char("aeiou")


# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for i in s:
#         if i in vowels:
#             count += 1
#     return count
# result = count_vowels("shubham")
# print(result)


# def sum_upto(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += i
#     return sum
# result = sum_upto(7)
# print(result)


# def is_digit(ch):
#     if ch.isdigit():
#         return True
#     else:
#         return False
#
#
# def count_digits(s):
#     count = 0
#     for char in s:
#         if is_digit(char):
#             count += 1
#     return count
#
#
# result = count_digits("ab12c3")
# print(result)


# def square(num):
#     return num * num
# def print_square(num):
#     result = square(num)
#     print(result)
# print_square(5)


# FUNCTION CALLING FUNCTION
# def is_even(num):
#     if num % 2 ==0:
#         return True
#     else:
#         return False
#
#
# def print_value(num):
#     if is_even(num):
#         print("Even")
#     else:
#         print("Odd")
#
# print_value(7)

#
# def check_positive(r):
#     if r > 0:
#         return True
#     else:
#         return False
#
# def print_result(p):
#     if check_positive(p):
#         print("Positive")
#     else:
#         print("Negative")
# print_result(-1)


# recursion function
# def sum_n(n):
#     if n == 0:
#         return 1
#     return n * sum_n(n-1)
#
# print(sum_n(5))


# variable length arguments
# def add(*numbers):
#     result = 0
#     for number in numbers:
#         result += number
#     return result
# print(add(10,20,30,40,50,60))
# print(add(1,2,3,4,5))

# s = [1,2,3,4,5,6]
# result = (sorted(s,reverse =True))
# print(result)

# result = list(filter(lambda n : n % 2 == 0,s))
# print(result)


# result = list(map(lambda a: a*5,s))
# print(result)


# nums = [1, 2, 3, 4]

# result = reduce(lambda a, b: a + b, nums)
# print(result)

# def greet(name, age):
#     return (age , name)
#
# result = greet(age=20, name="Shubham")
# print(result)


# from functools import reduce
#
# nums = [2, 3, 4, 5]
#
# result = list(map(lambda a:reduce(lambda a,b: a*b,range(1,a+1)),nums))
#
# print(result)

#
# a = ["10","20" ,"30"]
# result = list(map(lambda x:int(x),a))
# print(result)

# a =[121, 45, 33, 10, 99]
# result = list(filter(lambda x:x==(reversed(x)),a))
# print(result)


def show():
    print("Hello python")
show()

def sum(a,b):
    print(a+b)

sum(8,9)

def even_odd(a):
    if a % 2 == 0:
        print("even")
    else:
        print("odd")

even_odd(5)

def square(a):
    return a*a
s = square(8)
print(s)

def print_number(a):
    for i in range(a):
        print(i)
print_number(8)


x = 5
def show():
    x = 10
    print(x)

show()
print(x)















