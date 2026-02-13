s = {1,2,3,4,"Shubham"}
print(type(s))
s.add(23)
print(s)
s.remove("Shubham")
print(s)
print(99%5)
print(~-8)

a = 3
b = 4
c = 8
max = "a" if a > b and a > c else ("b" if b > a and b > c else c)
print(max)

if 0:
    print("Hello")
else:
    print("Hi")



s1 = {1,2,3,4}
s2 = {4,5,6,7}
print(s2-s1)