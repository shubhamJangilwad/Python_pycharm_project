# a = [70,25,77,11,34,56]
#
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]
# print(a)
from itertools import count
from operator import length_hint

# a = {
#     "a": 10,
#     "b": 120,
#     "z": 100
# }
# val = list(a.values())
# val.sort()
# tar = {}
# for val_ in val:
#     for k,v in a.items():
#         if a[k] == val_:
#             tar.update({k:v})
# print(tar)

#
# a = 345
# first = a % 10
# a = a // 10
#
# second = a % 10
# a = a // 10
#
# last = a % 10
#
# result = first + last
# print(result)
#
#
# word = "python"
# a = word[0] +" "+ word[-1]
# print(a)
#
#
# a = 782
# first = a % 10
# a = a // 10
# middle = a % 10
#
# print(middle)
#
# word = "hello"
# print(word[1:])
#
# word = "HELLO"
# print(word[1:-1])
#
# a = 384
# last = a % 10
# a = a // 10
# middle = a % 10
# a = a // 10
# first = a % 10
# if first %2 == 0 and last % 2 == 0:
#     print("Both Even")
# else:
#     print("Not Both Even")
#
#


# num = int(input("Enter a number: "))
# if num > 0:
#     print("positive")
# elif num < 0:
#     print("negative")
# else:
#     print("zero")
#
#
# char = input("Enter a character: ")
# if char.isalpha():
#     print("alphabet")
# elif char.isdigit():
#     print("digit")
# else:
#     print("special character")
#
#
# str = input("Enter a string: ")
# word = "python"
# if word in str:
#     print("yes")
# else:
#     print("no")
#
# for num in range(1,21):# check this program
#     if num %3 != 0:
#         print(num)
#         continue
#     if num == 15:
#         break
#
# text = "python123"
# letter1 = 0
# for letter in text:
#     if letter.isalpha():
#         print(letter)
#         letter1 = letter1 + letter
#
#

# str = input("Enter a string : ")
# if str.isalpha():
#     print("alphabets",str)
# elif str.isdigit():
#     print("digits",str)
# elif str.isalnum():
#     print("alphanumeric",str)



# word = "python"
# lenofword = len(word)-1
# i = 0
# while lenofword >= i:
#     print(word[lenofword],end = "")
#     lenofword -= 1


# prime number check
# number = int(input("Enter a number: "))
# count= 0
# for i in range(1, number + 1):
#     if number % i == 0:
#         count += 1
# if count == 2:
#     print("prime")
# else:
#     print("not prime")


# number = int(input("Enter a number: "))
# if number%5==0 and number%7==0:
#     print("divisible")
# else:
#     print("not divisible")


# count vowels and  consonants in the string
# a = input("Enter a string :")
# countv = 0
# countc = 0
# vowels = "aeiouAEIOU"
# for i in a:
#     if i in vowels:
#         countv += 1
#     else:
#         countc += 1
# print("vowels",countv)
# print("consonants",countc)


# num = 5
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()


# text = input("Enter a string: ")
# digit_count = 0
# valid = True
#
# for ch in text:
#     if not ch.isalnum():
#         valid = False
#         break
#     if ch.isdigit():
#         digit_count += 1
#
# if valid and digit_count >= 1:
#     print("valid")
# else:
#     print("invalid")


# a = input("Enter a string: ")
# count_upper = 0
# count_lower = 0
# count_digit = 0
# for char in a:
#     if char.isupper():
#         count_upper += 1
#     if char.islower():
#         count_lower += 1
#     if char.isdigit():
#         count_digit += 1
# print(count_upper)
# print(count_lower)
# print(count_digit)

# a = input("Enter a string: ")
# lenofa = len(a)-1
# i = 0
# while lenofa >= i:
#     print(a[lenofa], end="")
#     lenofa = lenofa-1


# #PASSWORD CHECK
# password = input("Enter your string: ")
# lenofp = len(password)
# countal = 0
# countdi = 0
# for letter in password:
#     if letter.isalpha():
#         countal += 1
#     if letter.isdigit():
#         countdi += 1
# if countal > 1 and countdi > 1 and lenofp >= 6:
#     print("strong")
# else:
#     print("weak")

# for row in range(1,6):
#     for col in range(5,row-1,-1):
#         print(col,end=" ")
#     print()


# numbers = [7,6,5,8,9,8]
# max = -1
# smax = -1
# for number in numbers:
#     if number > max:
#         max = number
#     if number > smax and number < max:
#         smax = number
# print(smax)
# print(max)

string = "aabbcccdccaaab"
dict = {}
max = -1
smax = -1
for char in string:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

#     count = dict[char]
#     if count > max:
#         max = count
# if count > smax and count < max:
#      smax = count
# print(dict)
# print(max)
# print(smax)


# for values in dict.values():
#     if values > max:
#         max = values
#     if values > smax and values < max:
#         smax = values
# print(dict)
# print(smax)

# for i in range(1,101):
#     if i % 2 == 0:
#         print(i)

s = int(input("Enter numbers"))
reverse = 0
l = 0
while s > 0:
    last = s % 10
    l += last
    s = s // 10

print(l)



