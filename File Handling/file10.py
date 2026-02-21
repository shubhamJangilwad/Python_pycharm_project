with open("contains.txt","r") as f:
    x = f.read()

with open("show.txt","w") as f:
    for i in x.split():
        if int(i) % 2 != 0:
            f.write("\n" ,i)
            print()

