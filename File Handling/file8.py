with open("contains.txt","a+") as f:
    for i in range(6):
        a = input("Enter str:")
        f.write(a + "\n")

with open("contains.txt","r") as f:
    dict = {}
    for i in f.readlines():
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for i,k in dict.items():
        print(i,k)