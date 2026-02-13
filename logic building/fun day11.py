# a =["12", "5", "abc", "9"]
# result = list(map(lambda x:int(x) if x.isdigit() else x ,a))
# print(result)
from functools import reduce

# a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# result = list((filter(lambda x:x%3==0,a)))
# print(result)

# a = [10, 45, 2, 89, 23]
# result = reduce(lambda x,y:x if x>y else y,a)
# print(result)


# a = [1, 2, 3, 4, 5, 6]
# even = filter(lambda x:x%2==0,a)
# result = list(map(lambda x:x*x,even))
# print(result)