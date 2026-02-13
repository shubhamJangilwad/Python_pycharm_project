# #01/01/26
s = input("Enter a string:")
digit_found = False
count = 0
vowels = 'aeiouAEIOU'
for char in s:
    if digit_found:
        digit_found = True
        break
    elif char in vowels:
        count += 1
if digit_found and char in vowels:
    print(count) # why this program not run tell me reason and explain step by step and without outer if program run

 # Build String of Only Alphabets
s = input("Enter a string:")
result = ""
for char in s:
    if char.isalpha():
        result = result + char
print(result)



s = input("Enter a string:")
count_lower = 0
count_upper = 0
for char in s:
    if char.islower():
        count_lower += 1
    elif char.isupper():
        count_upper += 1
if count_lower >=1 and count_upper >= 1:
    print("Yes")
else:
    print("No")


s = input("Enter a string:")
for char in range(len(s)-1):
    print(s[char],end="")
    if s[char] == s[char + 1 ]:
        break

s = input("Enter a string")
count_digit =0
alpha_found = False
for char in s:
    if alpha_found:
        alpha_found = True
    elif char.isdigit():
        count_digit += 1
if alpha_found and char.isdigit():
    print(count_digit)



