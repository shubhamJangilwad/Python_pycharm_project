# tell()  and Seek()
with open("contains.txt","r") as f:
    print(f.read(3))
    print(f.tell())

with open("contains.txt","r") as f:
    f.read(1)
    print(f.tell())
    f.seek(3)
    print(f.read(2))