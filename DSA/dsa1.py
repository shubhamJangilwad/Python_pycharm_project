# sum of numbers
numbers = [5, 10, 15, 20]

total = 0

for i in numbers:
    total = total + i

print("Sum is:", total)

# count even numbers
numbers = [1, 2, 3, 4, 5, 6]
count_even = 0
for i in numbers:
    if i % 2 == 0:
        count_even += 1

print("Even count = ",count_even)

# largest number
numbers = [10, 5, 25, 8, 15]
large = numbers[0]
for i in numbers:
    if i > large:
        large = i
print("Largest = ",large)

# second largest
numbers = [10, 5, 25, 8, 15]
large = numbers[0]
s_large = numbers[0]
for i in numbers[1:]:
    if i > large:
        s_large = large
        large = i
    elif i > s_large:
        s_large = i
print("Second Largest = ",s_large)