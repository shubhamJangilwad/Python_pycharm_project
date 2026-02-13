#30/12/25
from itertools import count

# Take a string and:
# Count how many characters are uppercase, lowercase, and digits
s = input("Enter a string:")
count_upper = 0
count_lower = 0
count_digit = 0
for char in s:
    if char.isupper():
        count_upper += 1
    elif char.islower():
        count_lower += 1
    elif char.isdigit():
        count_digit += 1
    else:
        print("special character")
print(count_upper)
print(count_lower)
print(count_digit)


# Build a new string that removes spaces and digits
# Keep only alphabets
s = input("Enter a string")
for char in s:
    if char.isalpha():
        print(char,end="")


# Take 5 numbers from user:
# Store in a list
# Create a new list that contains only even numbers
numbers = 5
a = []
b = []
for number in range(numbers):
    number = int(input("Enter the number:"))
    a.append(number)
    if number % 2 == 0:
        b.append(number)
print(a)
print(b)




# Count how many times 2 appears
# Print the index of first 2
t = (1,2,3,2,4,2)
count = 0
for num in t:
    if num == 2:
        count += 1
print(count)
print(t.index(2))


# Convert it to a set
# Print the unique values
# Explain why order changes
a = [1, 2, 2, 3, 4, 4, 5]
b = set(a)
print(b)
# order changes because in set insertion order not maintained


# Count Digits Until Alphabet
s = input("Enter a string:")
count_digit = 0
for char in s:
    if char.isalpha():
        break
    elif char.isdigit():
        count_digit += 1
print(count_digit)


# when found character then count digits
start = False
count = 0

for ch in s:
    if ch.isalpha():
        start = True
    elif start and ch.isdigit():
        count += 1


# Print Only Lowercase Letters
s = input("Enter a string:")
for char in s:
    if char.islower():
        print(char,end="")

# Check All Characters Are Alphanumeric
s = input("Enter a string:")
valid = True
for char in s:
    if not char.isalnum():
        valid = False
        break
if valid:
    print("valid")
else:
    print("invalid")

# Build String Until Space Found
s = input("Enter a string:")
result = ""
for char in s:
    if char == " ":
        break
    else:
        result = result + char
print(result)


# Stop on Digit Followed by Digit
s = input("Enter a string:")
for char in range(len(s)-1):
    print(s[char],end="")
    if s[char].isdigit() and s[char + 1].isdigit():
        break

















