# word = "developer"
# vowels = "aeiou"
# count = 0
#
# for letter in word:
#     if letter in vowels:
#         count += 1
#         if count == 3:
#             print(letter)
#             break
from unicodedata import digit

# extract the first digit only
# a = 789
# num = 0
# digit = a % 10
# num = a // 10
# digit = num % 10
# num = num // 10
# print(num)

# check middle digit is even or odd
# a = 246
# num = 0
# digit = a %10
# num = a // 10
# digit = num % 10
# num = a // 10
# print(digit)
# if digit%2==0:
#     print("even")
# else:
#     print("odd")

# text = "hello"
# ans = text.replace("e", "@")
# print(ans)


# word = "banana"
# vowels = "aeiou"
# count = 0
# for letter in word:
#     if letter in vowels:
#         count += 1
# print(count)

# a = 56
# b = 23
# smaller = a if a < b else b
# print(smaller)

# word = "PYTHON"
# c = (word[0].lower() + word[1:].upper())
# print(c)

# for letter in word:
#     if letter[0] != word.lower():
#         print(letter[0].lower())
#         break

# a = 1234
# digit1 = a % 10
# num1 = a // 1000
# print(digit1 + num1)


# a = 482
# last = a % 10
# a = a // 10
# middledigit = a % 10
# a = a // 10
# print(a + middledigit)


# a = 563
# last = a % 10 # last digit 3
# a = a // 10 # 3 seprated
# middle = a % 10 # middle digit 5
# a = a // 10 # 5 sperated
# first = a % 10 # first digit 7
# if first > last:
#     print("Yes")
# else:
#     print("No")
#
# result = last*100+middle*10+first
# print(result)

# a = 19
# b = 28
#
# num = a % 10
# num1 = b % 10
# if num == num1:
#     print("Equal")
# else:
#     print("Not Equal")


# name = "HELLO"
# c = name[:4]+name[4:].lower()
# print(c)



# word = "banana"
#
# # Step 1: Find first 'a'
# first = word.find("a")          # gives index 1
#
# # Step 2: Find second 'a'
# second = word.find("a", first+1)  # search after first 'a'
#
# # Step 3: Replace ONLY second 'a'
# result = word[:second] + "@" + word[second+1:]
#
# print(result)



# text = "banana"
# first = text.find("a")
# second = text.find ("a",first+1)
# third = text.find("a",second+1)
# print(text.replace("a", ""))

# word = "python"
# c = word[len(word)//2]
# if len(word) %2 == 0:
# 	print("no middle")
# else:
# 	print("middle")

# word = "A1B2C3"
# a= "a1"
# for char in word:
#     if 'a' <= char.lower() <= 'z':
#         print(char)

# word = "helllo123jhj23hghj32hgvg1"
# sum = 0
# for char in word:
#     print(type(char))
# #     if char in [str(i) for i in range(10)]:
# #         # print(char)
# #         sum += int(char)
# #     else:
# #         if sum>0:
# #             print(sum)
# #         sum=0
# # if sum > 0:
# #     print(sum)
# # # print(sum)

# a = 67834256789254637843299


# a = 123
# b = str(a)
# for char in b:
#     print(char)
# print()

# word = "python123"
# for letter in word:
#     if "0"<=letter<="9":
#         print(letter, end="")


# word = "abc45"
# sum = 0
# for letter in word:
#     if "0"<=letter<="9":
#         print(int(letter))
#         sum += int(letter)
# print(sum)


# word = "python5"
# num = int(word[-1])
#
# if num % 2 != 0:
#     print(word[:-1] * 5)
# else:
#     print(word[:-1] * 2)


# a = 90865454675456579
# b = str(a)
# largest = 0
# for char in b:
#     if int(char) > largest:
#         largest = int(char)
# print(largest)
# print(max([int(i) for i in str(a)]))

# word = "hello123"
# sum = 0
# for char in word:
#     if char.isdigit():
#         sum += int(char)
# print( sum)


# a = 345
# b = str(a)
# c = (b[len(b)//2])
# print(c)
# if int(c)%2 == 0:
#     print("even")
# else:
#     print("odd")


# word = "A9B8C7"
# for letter in word:
#     if letter.isdigit():
#         print(letter, end='')


# a = 1221
# real = a
# ispalindrome = False
# last = a % 10
# a = a // 10
# s_last = a % 10
# a = a // 10
# second = a % 10
# a = a // 10
# first = a % 10
# result = last*1000+s_last*100+second*10+first*1
# if real == result:
#     print("is palindrome")
#     ispalindrome = True


# word = "1342ofjwofweljfwfwiewe343240230@#$%&*"
# for letter in word:
#     if letter.isalnum():
#         print(letter)


# number = int(input("Enter a number: "))
# for num in range(0, number + 1):
#     if num % 2 != 0:
#         if num % 5 != 0:
#             print(num)


# optimization
# a = "shubham moreshwar jangilwad"
# countdigit =0
# dict = {}
# space = " "
# for char in a:
#     if char == space in dict:
#         dict[char] += 1
#     else:
#         dict[char] = 1
# print(dict)
# print(dict["s"])



# a = input("Enter a string: ")
# b = len(a)-1
# for char in a:
#     if char.isalpha() and b >= 4:
#         print("valid")
#         break
#     else:
#         print("invalid")
#         break

# n = 5
#
# for row in range(n,0,-1):
#     for col in range(n-row+1):
#         print(row,end = " ")
#     print()



# characters = input("Enter a string")
# lower = True
# for char in characters:
#     if not char.islower():
#         lower = False
#         break
# if lower and char.isalpha():
#     print("yes")
# else:
#     print("no")


# 20/12/25
# 1
# number = int(input("Enter a number:"))
# for num in range(1, number + 1):
#     if num % 6 ==0:
#         if num % 12 != 0:
#             print(num)


# 2
# s = input("Enter a string: ")
# count_upper = 0
# count_lower = 0
# count_digit = 0
# for char in s:
#     if char.isupper():
#         count_upper += 1
#     if char.islower():
#         count_lower += 1
#     if char.isdigit():
#         count_digit += 1
# print("Upper case :",count_upper)
# print("Lower case :",count_lower)
# print("number of digits :",count_digit)


# 3
# for row in range(1,6):
#     for col in range(1,row+1):
#         print(col,end="")
#     print()


# 21/12/25
#1
# numbers = int(input("Enter a number :"))
# for number in range(1, numbers + 1):
#     if number % 5 == 0:
#         if number % 10 != 0:
#             print(number)


# 2
# s = input("Enter a string: ")
# digitpresent = True
# for char in s:
#     if char.isdigit():
#         digitpresent = False
#         break
# if digitpresent and len(s) > 4:
#     print("valid")
# else:
#     print("invalid")

# 3
# s = input("Enter a string: ")
# alphacount = 0
# digitcount = 0
# spacecount = 0
# for char in s:
#     if char.isalpha():
#         alphacount += 1
#     elif char.isdigit():
#         digitcount += 1
#     elif char.isspace():
#         spacecount += 1
#     else:
#         print("Not a valid character")
#
# print("Alpha count :",alphacount)
# print("Digit count :",digitcount)
# print("Space count :",spacecount)

# 4
# for num in range(1,51):
#     if num % 18 == 0:
#         break
#     if num % 4 == 0:
#         continue
#     print(num)


# 5
# for row in range(5,0,-1):
#     for col in range(5,row-1,-1):
#         print(col,end="")
#     print()

# user = int(input("Enter How munch numbers you want to add : "))
# a = []
# for num in range(user):
#     s = int(input("Enter number:"))
#     a.append(s)
# print("the list is : a = ",a)


# bubble sort
# a = [5,1,4,8,2]
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if a[i] > a[j]:
#             temp = a[i]
#             a[i] = a[j]
#             a[j] = temp
#     print(a)


# 22/12/25
# a = []
# negative = True
# for num in range(5):
#     n = int(input("Enter a number: "))
#     if n < 0:
#         negative = False
#         print("negative found")
#     else:
#         print("no negative ")
#         a.append(n)
# print(a)

# s = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# a = []
# for char in s:
#     if char in vowels:
#         a.append(char)
# print(a)


# nums = [10, 15, 20, 25, 30, 35]
# a = []
# for num in nums:
#     if num % 5 == 0:
#         if num % 10 != 0:
#             a.append(num)
# print(a)


# a = []
# for num in range(10):
#     n = int(input("Enter a number: "))
#     if n == 0:
#         break
#     if n % 3 == 0:
#         continue
#     a.append(n)
#
# print(a)

# a = []
# for num in range(5):
#     n = int(input("Enter a number: "))
#     if n % 2 == 0:
#         a.append(n)
# print(a)

# x = [4, 1, 3, 2]
# x.reverse()
# x.sort()
# print(x)
