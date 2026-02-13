# f = open("C:\\Users\\shubh\\PyCharmMiscProject\\logic building\\Daily_logic_building\\logic building\\day1.py","r")
# print(f.read())
# f.close()

with open("hello.txt","r") as f:
    c = f.readlines()
    count_lines = 0
    for i in c:
        print(i)
        count_lines += 1
print(count_lines)




