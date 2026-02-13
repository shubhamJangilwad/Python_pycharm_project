from operator import index

s = "Hello python"
print(s[0])
print(s[-1])
print(s[8:2:-1])

s1 = "  Hello Python    "
print(s1.lstrip())
print(s1.strip())
print(len(s1))

for i in s1[::-1]:
    print(i,end="")
print()
print(s1.index("l"))

s3 = "Good Morning"
for i in s3:
    print(i,s3.count(i))


print(s3.replace("G","g"))
print(s3.split())
print("".join(s3))
print(s3.swapcase())

for i in s3:
    if i.isalpha():
        print(i)


# text = 'python programming'
# print(text.upper())
#
# word = "developer"
# print(len(word))
#
#
# word = "This is a bad example"
# print(word.replace("bad", "good"))
#
# word = "apple banana mango"
# print(word.split())
#
# word = "banana"
# print(word.count("a"))
#
# word = "file.txt"
# print(word.endswith(".txt"))
#
# word = "Python Programming"
# print(word.startswith("Py"))
#
# word = "  hello  "
# print(word.strip())
#
# word = "HELLO"
# print(word[0:-1]+word[-1:].lower())
#
#
# word = "banana"
# first = word.find("n")
# print(first)
#
# word = "banana"
# print(word.index("n"))


# word = "good morning"
# lenofword = len(word)-1
# i = 0
# while i <= lenofword:
#     if word[i] == "o":
#         print(word[i],i)
#     i = i + 1