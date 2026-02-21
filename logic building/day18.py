data = [1,2,3,4,6,7,8]
b = max(data)
c = sum(data)
d = 0
for i in range(max(data)+1):
    d += i
b1 = d - sum(data)
print("missing:",b1)


a = input("Enter a string: ")
b = input("Enter a string: ")
is_equal = False
for i in a:
    if i in b:
        is_equal = True

if is_equal and len(a) == len(b):
    print("Anagram")
else:
    print("Not Anagram")

