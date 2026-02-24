def my_max(n):
    a = n[0]
    for i in n:
        if i > a:
            a = i
    return a

data = [1,2,3,4,6,7,8]
b = max(data)
c = sum(data)
d = 0
for i in range(max(data)+1):
    d += i
b1 = d - sum(data)
print("missing:",b1)


s1 = input("Enter a string: ")
s2 = input("Enter a string: ")
s3 = list(s1)
s4 = list(s2)
s3.sort()
s4.sort()
if s3 == s4:
    print("anagram")
else:
    print("not anagram")



# armstrong number
a = 153
original = a
count = 0
while a > 0:
    a = a // 10
    count += 1

temp = original
total = 0
while temp > 0 :
    num = temp % 10
    total += num ** count
    temp = temp // 10

if original == total:
    print("Armstrong")
else:
    print("Not armstrong")


c = "aaabbcdddd"
count = 1
for i in range(len(c)-1):
    if c[i] == c[i+1]:
        count += 1
    else:
        print(c[i] + str(count),end="")
        count = 1
print(c[-1]+str(count))


def add_numbers(n):
    add = 0
    for i in n:
        add += i
    return add

