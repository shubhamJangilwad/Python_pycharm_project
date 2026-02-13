#29/12/25

#Reverse Each Word , keep the order same
# s = input("Enter a string:")
# current = ""
# result = ""
# for char in s:
#     if char != " ":
#         current = char + current
#     else:
#         result = result + current + " "
#         current =""
# print(result + current)

# Stop on Two Same Characters
# s = input("Enter a string:")
# for char in range(len(s)-1):
#     print(s[char],end = " ")#printing the char before check
#     if s[char] == s[char + 1]:
#         break

# Alternating Uppercase & Lowercase
# s = input("Enter a string:")
# valid = True
# for char in range(len(s)-1):
#     if not s[char].islower() and s[char+1].isupper():
#         valid = False
# if valid:
#     print("valid")
# else:
#     print("invalid")


# Count Vowels Until Consonant
# s = input("Enter a string:")
# vowels = "aeiouAEIOU"
# count = 0
# for char in s:
#     if char not in vowels:
#         break
#     count += 1
# print(count)


# Build String by Skipping Every Second Character
# s = input("Enter a string")
# for char in range(len(s)):
#     if char % 2 == 0:
#         print(s[char])

# Reverse characters until digit
# s = input("Enter a string:")
# result = ""
# for char in s:
#     if char.isdigit():
#         break
#     print(char,end="")

# Remove consecutive duplicates
# s = input("Enter a string:")
# result = ""
# for char in range(len(s)-1):
#     if s[char] == s[char + 1]:
#         result = result + s[char]
# print(result+s[-1])

# Check whether characters alternate between lowercase and uppercase
# First character can be either case
# s = input("Enter a string:")
# valid = True
# for char in range(len(s)-1):
#     if not (s[char].islower() and s[char + 1].isupper() or
#         s[char].isupper() and s[char + 1].islower()):
#         valid = False
#         break
#
# if valid:
#     print("valid")
# else:
#     print("invalid")


# Stop on two consecutive vowels
# s = input("Enter a string:")
# vowels = "aeiouAEIOU"
# for char in range(len(s)-1):
#     print(s[char],end="")
#     if s[char] in vowels and s[char + 1] in vowels:
#         break



