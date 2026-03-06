#Duplicate remover

data = [10, 20, 10, 30, 40, 20, 50]
data1 = []
for nums in data:
    if nums not in data1:
        data1.append(nums)
print(data1)

# character frequency
a = "programming"
d = {}
for ch in a:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

print(d)


def my_reduce(function, iterable):
    result = iterable[0]
    for item in iterable[1:]:
        result = function(result, item)
    return result

print(my_reduce(lambda x, y: x + y, [1,2,3,4]))




data = [10, "20", 30.5, "abc", True, False, "40"]
ch = "abcdefghijklmnopqrstuvwxyz"
total_sum = 0
for i in data:
    if type(i) == int and type(i) != bool:
        total_sum += i
    elif type(i) == str and i not in ch:
        total_sum += int(i)
    elif type(i) == float:
        total_sum += int(i)

print(total_sum)


numbers = [5, 12, 7, 20, 3]

result = list(map(lambda x: x*x if x > 10 else x*x*x,numbers))
print(result)




# nested list
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

data = [1, [2,3], [4,[5,6]], 7]
print(flatten(data))






















