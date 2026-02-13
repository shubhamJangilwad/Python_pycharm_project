# f = open("add.txt","a")
# f.write("\n old file data present and this line add")
# f.write("\n This is new data")
# f.close()

with open("hello.txt","a") as f:
    f.write("\nLearning File Handling")
