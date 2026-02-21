# do this type program regularly
with open("contains.txt","w") as f:
    for i in range(1,11):
        f.write(str(i)+"\n")


with open("contains.txt","r") as f:
    data = f.readlines()

    for line in data:
        x = int(line.strip()) # it removes the \n or spaces between lines
        if x % 2 ==0:
            print(x)
