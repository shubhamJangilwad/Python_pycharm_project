26/12/25

s = input("Enter a string:")
count = 0

for char in s:
    if not char.isdigit():
        if not char.isalpha():
            count += 1
print(count)


s = input("Enter a string:")
valid = False
for char in s:
    if s.count(char) <=1 :
        valid = True
        break
if valid:
    print(char)
else:
    print("No unique character")


s = input("Enter a string: ")

current_word = ""
result = ""

for char in s:
    if char != " ":
        current_word = char + current_word
    if char == " ":
        result = result + current_word + " "
        current_word = ""

result = result + current_word
print(result)



s = input("Enter a string:")
count = 0
for char in s:
    if char.isdigit():
        break
    if char.isupper():
        count += 1
print(count)



s = input("Enter a string:")
current_word = ""
result = ""
for char in s:
    if char != " ":
        current_word = char + current_word
    if char == " ":
        result = result + current_word + " "
        current_word = ""
print(result + current_word)


s = input("Enter a string:")
a = ''
for char in range(len(s)-1):
    if s[char] != s[char+1]:
        a = a + s[char]

a = a + s[-1]
print(a)




s = input("Enter a string:")
vowels = "aeiouAEIOU"
consonants = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
valid = True
for char in range(len(s)-1):
    if (s[char] in vowels and s[char + 1] in consonants) and (s[char] in consonants and s[char + 1] in vowels):
        valid = False
if valid:
    print("valid")
else:
    print("invalid")


a = int(input("Enter the numbers:"))
s = 0
count  = 0
while a > 0:
    s = a % 10 #
    a = a // 10

    count += 1

print(count)


s = input("Enter a string:")
vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
valid = True
for char in range(len(s)-1):
    if (s[char] in vowels and s[char + 1] in vowels) or (s[char] in consonants and s[char+1] in consonants):
        valid = False
        break
if valid:
    print("valid")
else:
    print("invalid")















