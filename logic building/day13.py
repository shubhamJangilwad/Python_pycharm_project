#09/01/26
# List → Tuple Conversion with Condition
nums = [1, 2, 2, 3, 4, 5, 5]
nums1 = []
for i in nums:
    if i not in nums1:
        nums1.append(i)
print(tuple(nums1))

data = [10, (1,2), {3,4}, [5,6],[7,8,9], "hi", {"a":1}]
b = 0
count_list = 0
count_tuple = 0
count_set = 0
count_dict = 0
for i in data:
    if type(i) == list:
        count_list += 1
        b = len(i)+b
    elif type(i) == tuple:
        count_tuple += 1
    elif type(i) == set:
        count_set += 1
    elif type(i)== dict:
        count_dict += 1
print(count_list)
print(count_tuple)
print(count_set)
print(count_dict)
print(b)

# Dictionary with List Values
marks = {
    "math": [45, 60, 30],
    "science": [70, 80],
    "english": [25, 35, 40]
}

for key, value in marks.items():
    for m in value:
        if m >= 40:
            print(key)
            break


t = (1, "2", 3.5, 4, "hi", 6)
t1 = set()
for i in t:
    if type(i) == int:
            t1.add(i)
print(t1)

# List of Dictionaries
students = [
    {"name": "A", "age": 20},
    {"name": "B", "age": 17},
    {"name": "C", "age": 22}
]
