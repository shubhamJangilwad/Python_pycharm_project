#17/02/26
# second_largest number
data = [10, 45, 23, 89, 45, 67, 89]
lar = 0
s_lar = 0
for i in data:
    if i > lar:
        s_lar = lar
        lar = i
    elif s_lar < i < lar:
        s_lar = i
print(s_lar)



# pallindrome
a = input("Enter a string: ")
rev = ""
for i in a:
    rev = i + rev
if rev == a:
    print("Pallindrome")
else:
    print("not pallindrome")

# separate data types
data = [10, "hi", 3.5, True, 7, "python", False, 2.2]
integer = []
string = []
flo  = []
boolean = []
for i in data:
    if type(i) == int and type(i) != bool:
        integer.append(i)
    elif type(i) == str:
        string.append(i)
    elif type(i) == float:
        flo.append(i)
    elif type(i) == bool:
        boolean.append(i)

print(integer)
print(string)
print(flo)
print(boolean)


# count words in sentence
a = "Python is very very easy language"
b = a.split()
di = {}
for i in b:
    if i in di:
        di[i] += 1
    else:
        di[i] = 1

for i,k in di.items():
    print(i,k)



# cubes of iterations
a = [1,2,3,4,5]
result = list(map(lambda x:x*x*x ,a))
print(result)

# pattern
for i in range(1,6):
    for k in range(i):
        print(i,end="")
    print()


# average of marks
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average_marks(self):
        add = 0
        count = 0
        for i in self.marks:
            if i >= 0:
                add += i
                count += 1


        average = add // count
        return average

s = Student("shubham",[50,60,70,80])
print("average of marks",s.average_marks())

#exception handling
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if b < 0:
        print("invalid input")
    else:
        print(a//b)
except ZeroDivisionError:
    print("zero division error")


