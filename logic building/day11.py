#07/01/26
# count int,str and others
# data = [10, "hi", 3.5, "5", True, "python"]
#
# count_int = 0
# count_str = 0
# count_others = 0
#
# for i in data:
#     if type(i) == int and i is not True:
#         count_int += 1
#     elif type(i) == str:
#         count_str += 1
#     else:
#         count_others += 1
#
# print(count_int)
# print(count_str)
# print(count_others)


# sum till alph got
# a =  "1234abc56"
#
# result = 0
# for ch in a:
#     if ch.isdigit():
#         result = result + int(ch)
#     elif ch.isalpha():
#         break
#
# print(result)



# create new list with unique values
# nums = [1, 2, 2, 3, 4, 3, 5]
# a = set()
# for i in nums:
#     a.add(i)
# print(list(a))


# print subjects that marks >= 40
# marks = {"math": 78, "science": 35, "english": 64, "history": 40}
# for key,value in marks.items():
#     if value >= 40:
#         print(key)


# if ch is digit skip and if even index ch print
# s = input("Enter a string: ")
# for ch in range(len(s)):
#     if s[ch].isdigit():
#         continue
#     elif ch % 2 == 0 :
#         print(s[ch])


# Create three lists: integer,string,others
# items = [1, "apple", 2.5, "3", False, "hi", 10]
# integer = []
# string = []
# others = []
# for i in items:
#     if type(i)== int:
#         integer.append(i)
#     elif type(i)==str:
#         string.append(i)
#     else:
#         others.append(i)
# print(integer)
# print(string)
# print(others)


# Count Until Space
# a = "hello world"
# count = 0
# for ch in a:
#     if ch != " ":
#         count += 1
#     elif ch == " ":
#         break
# print(count)


# Digits Product
# a = "a2b3c4"
# found = False
# result = 1
# for i in a:
#     if i.isdigit():
#         result = result * int(i)
#     found = True
# if found:
#     print(result)
# else:
#     print(0)
#


# First Non‑Repeating Character
# s = input("Enter a string: ")
# for i in s:
#     if s.count(i) == 1:
#         print(i)
#         break


# Skip Vowels at Odd Index
# s = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# for i in range(len(s)):
#     if s[i] in vowels and i % 2 == 1:
#         continue
#     elif i % 2 == 1:
#         print(s[i])














