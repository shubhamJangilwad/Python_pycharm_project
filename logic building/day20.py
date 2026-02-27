#26/02/26
from itertools import count

data1 = []
rev = ''
data = [10, "hello", 3.5, True]
for i in data:
    if type(i) == int and type(i) != bool:
        data1.append(i*2)
    elif type(i) == str:
        data1.append(i[::-1])
    elif type(i) == float:
        data1.append(int(i))
    elif type(i) == bool:
        data1.append(str(i))
print(data1)


# check type and store in dictionary
data3 = [10, 20.5, "hi", 5, "python", 3.14, False]
data = {
    "integer" : 0,
    "string" : 0,
    "float" : 0,
    "boolean" : 0

}
for i in data3:
    if type(i) == bool:
        data["boolean"] += 1
    elif type(i) == int:
        data["integer"] += 1
    elif type(i) == str:
        data["string"] += 1
    elif type(i) == float:
        data["float"] += 1
print(data)

# using isinstance
# instance also checks type of value and it is flexible than type()
for i in data3:
    if isinstance(i,bool):
        data["boolean"] += 1
    elif isinstance(i,int):
        data["integer"] += 1
    elif isinstance(i,str):
        data["string"] += 1
    elif isinstance(i,float):
        data["float"] += 1
print(data)


# even numbers using lambda
numbers = [1,2,3,4,5,6,7,8,9,10]
result = list(filter(lambda x: x % 2 == 0 ,numbers))
print(result)

a =  "aabbcddee"
found = False
for i in a:
    if a.count(i) == 1:
        found = True
        break
if found:
    print(i)


def my_function(n):

    show = list(map(lambda x : x * 2 , n))
    return show
print(my_function([1,2,3,4,5,6]))


from functools import reduce

l = [1,2,3,4,5,6,7,8,9]
result = reduce(lambda a,b:a*b, l)
result1 = reduce(lambda x,y: x if x>y else y,l)
print(result)
print("max:",result1)
