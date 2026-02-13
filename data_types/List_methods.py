l1 = [2,4,6,7,8,9,10]
# indexing[]
# using index we can store and access the items from the list
l1[0]=12
print(l1)
print(l1[0])

# slice
# using slice we can get sublist of list , using slice reverse the list
# [start : end : steps]
print(l1[:])
print(l1[::-1])#reverse the string
print(l1[::2])

# using len function we can get lenght of the list(items in the list)
print(len(l1))

#append
# add the item/element in list at the end
l1.append(15)
print(l1)
l2 = [11,13,14,16]
l1.append(l2)
print(l1)

# remove
# using remove we can remove the item/element
l1.remove(l2)
l1.remove(4)
print(l1)

# insert
# store the value of specific index
l1.insert(0,5)
print(l1)

# extend
# add the element of one list another list
l1.extend(l2)
print(l1)
# Difference of "append" and "extend" is append take the list and add to the list as it is with [] square brackets but extend add the item from one list another list

# count
# using count we can count the items how many times item presents
l3 = [1,3,1,2,3,4,5,5,1]
l3.count(1)
print(l3.count(1))

# index function
# Returns the index of first occurrence of the specified item.
print(l3.index(5))

# pop()
# It is used to remove and return the last element of the list.
l4 = [1,2,3,4,5,6]
print(l4)
l4.pop()#remove the last  item one from the list
print(l4)
l4.pop()#removes the list last item one from the list
print(l4)
l4.pop(2)#using this we remove index item also
print(l4)

# reverse()
# We can use this reverse function to reverse the elements of given list
l4.reverse()
print(l4)


# sort()
# It is used to sort the elements of the list in natural order.
# Elements must be of same type otherwise error
l4.sort()
print(l4)
l4.sort(reverse=True)#using this we can sort the list in decending order
print(l4)


# Cloning
# We can perform cloning using copy() function.
# We can create a new list object using existing list using copy() function
l5 = [5,6,7,8,9,10]
y = l5.copy()
print(l5)
print(y)
print(id(l5))#using id build in function we can check the address of the object
print(id(y))

print(l5 is y)# is used for address comparison


# concatenation "+"
# using this operator we can add the items
print(l4)
print(l5)
print(l4 + l5)

# Multiplication "*"
print(l4)
print(l4 * 2) # answer is [4,2,1,4,2,1] multiple times the list items


# Clear() function
# It is used remove all the elements from the list

print(l4)
l4.clear()
print(l4)# using clear()function clear the list or removes the items from the list



