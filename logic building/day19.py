# from day18 import my_max
# print(my_max([1,2,3,4,5,6,7,8,9]))

a = "aabbccdde"
b = ''
for i in a:
    if i not in b:
        b = b + i
print(b)

b = "python"
rev = ''
for i in b:
    rev = i + rev
print(rev)

c = 12345
rev = 0
while c > 0:
    num = c % 10
    rev = rev * 10 + num
    c = c // 10

print(rev)



d = 'aaabbccccdaa'
count = 1
for i in range(len(d)-1):
    if d[i] == d[i + 1]:
        count += 1
    else:
        print(d[i]+str(count),end="")
        count = 1
print(d[-1]+str(count))



e = "madam"
rev = ''
for i in e:
    rev = i + rev
if e == rev:
    print("palindrome")
else:
    print("not palindrome")



f = input("Enter a string:")
g = input("Enter a string:")
f1 = ''
g1 = ''
for i in f:
    f1 = (i,f.count(i))
for k in g:
    g1 = (k,g.count(k))

if f1 == g1:
    print("Anagram")
else:
    print("Not Anagram")




h = "programing"
count  = 0
for i in h:
    if h.count(i) == 1:
        break
print(i)



data = [0,1,0,3,12,0,5]
data1 = []
data2 = []
for i in data:
    if i == 0:
        data1.append(i)
    else:
        data2.append(i)
print(data2+data1)





