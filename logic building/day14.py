# data = [1, [2, "3", 4], "hi", [5, 6], True, 7]
# add = 0
# add1 = 0
# add2 = 0
# for i in data:
#     if type(i) == int:
#         add += i
# print(add)
# for k in data[1]:
#     if type(k) == int:
#         add1 += k
# print(add1)
# for j in data[3]:
#     if type(j)== int:
#         add2 += j
# print(add2)
#
# print(add+add1+add2)
from six import integer_types

# data = [1, "hi", 2.5, "3", True, "python", 4]
# k  = []
# s = []
# f = []
# for i in data:
#     if type(i) == int:
#         k.append(i)
#     elif type(i) == str:
#         s.append(i)
#     elif type(i) == float:
#         f.append(i)
# print(k)
# print(s)
# print(f)

d = ("shubham is a good boy".split())
d.sort()
print(d)
d1 = {}
for i in d:
    if i  in d1:
        d1[i] += 1
    else:
        d1[i] = 1
print(d1)


x = (lambda y:y*y)
print(x(8))