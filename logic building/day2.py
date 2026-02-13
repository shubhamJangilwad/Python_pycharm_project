#24/12/25
s = input("Enter a string :")
countupper = 0
countlower = 0
countdigit = 0
for char in s:
    if char.isupper():
        countupper += 1
    elif char.islower():
        countlower += 1
    elif char.isdigit():
        countdigit += 1

print(countupper)
print(countlower)
print(countdigit)


s = input("Enter a string:")
for char in s:
    if s.count(char)>1:
        print(char)
        break
    else:
        print("no repetition")


s = input("Enter a string:")
for char in s:
    if not char.isalpha():
        continue
    print(char,end="")
print()


s = input("Enter a string:")
for i in s:
    for j in s[::-1]:
        if i==j:
            print(i,j,end=" ")
if i == j:
    print("palindrome")
else:
    print("not palindrome")

s = input("Enter a string:")
found = False

for char in s:
    if s.count(char) > 1:
        print(char)
        found = True
        break

if not found:
    print("No repetition")




s = input("Enter a string:")
rev = ""

for char in s:
    rev = char + rev

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


number = int(input("Enter a number: "))
rev = 0
while number > 0:
    a = number % 10
    number = number // 10
    rev = rev * 10 + a
print(rev)



a = [8,7,2,5,3,1]
valid = False
for num in a:
    for j in a:
        if num + j == 10:
            valid = True
            break
if valid:
    print("True")
else:
    print("False")


s = input("Enter a string:")
rev = ""

for char in s:
    rev = char + rev

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")












