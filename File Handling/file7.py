# try:
#     with open("python.txt","r") as f:
#         print(f.read())
# except:
#     print("FileNOtFoundError")
#
# finally:
#     print("This is the end of the program")

with open("source.txt","r") as f:
    c = f.read()

with open("Destination.txt","w") as f:
    d = f.write(c)
    print(d)
