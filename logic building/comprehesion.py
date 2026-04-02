#List
#Transform - for every element return something
result = [i*2 for i in [1,2,3,4,5,6]]
print(result)

result = ["even" if i%2 == 0 else "odd" for i in [1,2,3,4,5,6]]
print(result)

#Filter - take only element that satisfy condition
#when we write condition at end means filtering

result = [i for i in range(1,11) if i%2==0]
print(result)




#Dictionary

result = {i: i+1 for i in [1,2,3]}
print(result)

result = {i: i*i for i in range(3)}
print(result)

result = {i:i*i*i for i in range(1,4)}
print(result)

result = {i: "even" if i%2==0 else "odd" for i in range(1,4)}
result = {i*i for i in range(1,6) if i%2==0}
fruits = ["apple","banana"]
result = {fruit:len(fruit) for fruit in fruits}
#set

result = {i for i in [1,2,2,3]}
print(result)

result = {i for i in [1,2,3,4,5] if i>3}
print(result)

























