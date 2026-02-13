# 23/12/25
a = input("Enter a string: ")
countalpha = 0
countdigit = 0
for char in a:
    if char.isalpha():
        countalpha += 1
    elif char.isdigit():
        countdigit += 1
print(countalpha)
print(countdigit)


s = input("Enter a string:")
vowels = "aeiouAEIOU"
found = False
for char in s:
    if char in vowels:
        found = True
        break
if found :
    print("vowel found")
else :
    print("No vowel")


a = "shubham"
vowels = "aeiouAEIOU"
for char in a:
    if char not in  vowels:
        print(char)
        if char in vowels:
            continue


a = "shubham"
for i in range(len(a)-1,-1,-1):
    print(a[i])

a = "shubham"
for char in range(0,len(a)):
    if a[char].isdigit():
        break
    if char % 2 == 0:
        print(a[char])

sum = 0
n = int(input("Enter a number: "))
for i in range(1,n):
    if n % i == 0:
        sum = sum + i
if sum == n:
    print("Yes, the" ,n, " is a perfect number.")
else:
    print("No, the ",n," is not a perfect number.")

for n in range(1, 1001):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum = sum + i
    if sum == n:
        print(n)
