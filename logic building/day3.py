#25/12/25

s = input("Enter a string:")
countv = 0
countc = 0
vowels = "aeiouAEIOU"
for char in s:
    if char in vowels:
        countv += 1
    elif char not in vowels and char.isalpha():
        countc +=1
print("vowels:",countv)
print("consonants:",countc)

s = input("Enter the strings:")
count = 0
counts = 0
a = "abcdefghijklmnopqrstuvwxyz"
c = " "
for char in s:
    if char in a:
        count += 1
        if char in c:
            break

print(count)


s = input("Enter the strings:")
maxs = 0
word = ''
bucket = []
for char in s:
    if not char == ' ':
        word += char
    if char == ' ':
        bucket.append(word)
        word = ''
bucket.append(word)
for i in bucket:
    if len(i) > maxs:
        maxs = len(i)
print(maxs)


s = input("Enter a string:")
t = input("Enter a char:")
count = 0
for char in s:
    if char == t:
        count += 1
print(count)


s = input("Enter a string:")
a = []
for char in s:
    if char:
        a.append(char)
print(set(a))
for i in set(a):
    print(i,end="")
print()



s = input("Enter a string:")
count = 0
for char in s:
    if char.isdigit():
        count += 1
    if count >= 3:
        break
    if char.isalpha():
        print(char)


s = input("Enter the string: ")

max_len = 0
current_len = 0

for char in s:
    if char != ' ':
        current_len += 1
    else:
        if current_len > max_len:
            max_len = current_len
        current_len = 0

# check last word
if current_len > max_len:
    max_len = current_len

print(max_len)


s = input("Enter a string:")
result = ""
prev = ""

for char in s:
    if char != prev:
        result += char
        prev = char

print(result)
print(prev)
