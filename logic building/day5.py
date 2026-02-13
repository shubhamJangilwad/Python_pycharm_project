#28/12/25

# Reverse each word, keep word order same
# a = input("Enter a string:")
# currentw =""
# result =""
# for char in a:
#     if char != " ":
#         currentw = char + currentw
#     else:
#         result = result + currentw + " "
#         currentw = ""
# print(result + currentw)
#
#
# Remove all digits, keep only alphabets, preserve order
# s = input("Enter a string")
# result =""
# for char in s:
#     if char.isalpha():
#         result = result + char
# print(result)
#
#
# Remove consecutive duplicate characters only
# s = input("Enter a string:")
# result = ""
# for char in range(len(s)-1):
#     if s[char] != s[char+1]:
#         result = result + s[char]
# print(result + s[-1])
#
#
# Remove all vowels, keep other characters as they are
# s = input("Enter a string:")
# vowels = "aeiouAEIOU"
# result = ""
# for char in s:
#     if char not in vowels:
#         result = result + char
# print(result)
#
#
# Reverse only the second half of the string.
# s = input("Enter a string: ")
# n = len(s)
# result = ""
#
# for i in range(n//2):
#     result += s[i]
#
# for i in range(n-1, n//2-1, -1):
#     result += s[i]
#
# print(result)

#
#
# Check whether a string has alternating digits and alphabets
# s = input("Enter a string:")
# valid = True
# for char in range(len(s)-1):
#     if  not ( (s[char].isalpha() and s[char + 1].isdigit()) or
#             (s[char].isdigit() and s[char + 1].isalpha())):
#         valid = False
#         break
#
# if valid:
#     print("valid")
# else:
#     print("invalid")

#
#
# Check whether no two digits are together in the string
# s = input("Enter a string:")
# valid = True
# for char in range(len(s)-1):
#     if s[char].isdigit() and s[char+1].isdigit():
#         valid = False
# if valid:
#     print("valid")
# else:
#     print("invalid")
#
#
# Stop the loop immediately if you find two consecutive consonants.
# Print characters until that point
# s = input("Enter a string:")
# vowels = "aeiouAEIOU"
#
# for char in range(len(s)-1):
#     print(s[char],end="")
#     if (s[char].isalpha() and s[char + 1].isalpha() and
#         s[char] not in vowels and s[char + 1] not in vowels):
#         break



# Check whether the string starts with lowercase and alternates case till the end
# s = input("Enter a string: ")
# valid = True
#
# if not s[0].islower():
#     valid = False
#
# for i in range(len(s) - 1):
#     if (s[i].islower() and s[i+1].islower()) or \
#        (s[i].isupper() and s[i+1].isupper()):
#         valid = False
#         break
#
# if valid:
#     print("Valid")
# else:
#     print("Not Valid")




