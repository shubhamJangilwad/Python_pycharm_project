# a = [10, 20, 30, 40, 50]
# print(a[0])
#
# a = [5, 15, 25, 35]
# print(a[-1])
#
# a  = [1, 2, 3, 4, 5]
# a[2]= 99
# print(a)
#
# a =  [10,20,30]
# a.append(40)
# print(a)
#
# a =  [1, 2, 3, 4]
# a.insert(2, 99)
# print(a)
#
# a = [10, 20, 30, 40]
# a.remove(20)
# print(a)
#
# a = [5, 10, 15, 20]
# a.pop(1)
# print(a)
#
# a = ["apple", "banana", "mango"]
# for ele in a:
#     print(ele)
#
# a = [2, 4, 6, 8, 10]
# print(len(a))
#
# a = [10, 20, 30, 40, 50]
# print(a[1:3])
#
#
# a = [1, 2]
# b = [3, 4]
#
# a.extend(b)
# print(a)


a = [3,6,9,12,12,13]
b = [2,4,6,90,87,6,7,8,9]
c = []
# output = [5,10,15]
if len(a) > len(b):
    for i in range(len(b)):
        c.append(b[i] + a[i])
elif len(b) > len(a):
    for j in range(len(a)):
        c.append(a[j] + b[j])

print(c)

# v = [10,[12,14,25,[11,15],10],20]
#
# a1 = v[1]
# a2 = a1[3]
# a3 = a2[1]
# for i in a2:
#     print(i)
x = 5
print(id(x))

print(str(False))

l = [1,2,3,4,5,6,7,8,9]
print(l)
l.reverse()
print(l)
