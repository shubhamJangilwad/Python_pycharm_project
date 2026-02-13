#05/01/26
from fontTools.misc.arrayTools import pointInRect

# s = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# consonants = "bcdfghhklmnpqrstvwxyz"
# countv = 0
# countc = 0
# for ch in s:
#     if ch in vowels:
#         countv += 1
#     elif ch in consonants:
#         countc += 1
# print(countv)
# print(countc)
#
# s= input("Enter a string:")
# found = False
# for ch in range(len(s)-1):
#     if s.count(s[ch])>1:
#         found = True
#         break
# if found:
#     print(s[ch])
# else:
#     print("no repetition")

# a = "python is very easy"
#
# words = []
# current = ""
#
# for ch in a:
#     if ch != " ":
#         current = current + ch
#     else:
#         words.append(current)
#         current = ""
#
# words.append(current)   # add last word
#
# for i in range(len(words)-1, -1, -1):
#     print(words[i], end=" ")

#count upppercase , lowercase and digit ignore spaces
# a = input("Enter a string:")
# countu = 0
# countl = 0
# countd = 0
# for ch in a:
#     if ch.isupper():
#         countu += 1
#     elif ch.islower():
#         countl += 1
#     elif ch.isdigit():
#         countd += 1
# print(countu)
# print(countl)
# print(countd)



# s = input("Enter a sentence: ")
# result = ""
# space_found = False
# for ch in s:
#     if ch != " ":
#         result = result + ch
#         space_found = False
#     else:
#         if not space_found and result != "":
#             result = result + " "
#             space_found = True
# print(result)


# Count Words in a Sentence
# s = input("Enter a string")
# space_found = False
# count = 0
# result = ""
# for ch in s:
#     if ch != " ":
#         result = result + ch
#         space_found = False
#         count += 1
#     else:
#         if not space_found and ch != "":
#             result = result + " "
#             space_found = True
# print(count)


# first repeated character
# s = input("Enter a string")
# count_repeated_char = 0
# for ch in s:
#     if s.count(ch)== 2:
#         print(ch)
#         break

# reverse only digits
# s = input("Enter a string")
# result = ""
# for ch in s:
#     if ch.isdigit():
#         result = ch + result
#     elif not ch.isdigit():
#         result = result + ch + result
# print(result)

#
# for i in range(1,51):
#     if i % 5 == 0:
#         print("Fizz")
#
#     if i % 7 == 0:
#         print("Buzz")
#
#     if i % 5 == 0 and i % 7 == 0:
#         continue


s = input("Enter a string: ")
result = ""
for ch in s:
    result = ch + result
if s == result :
    print("Palindrome")
else:
    print("not palindrome")