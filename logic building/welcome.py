# rows = 6
# for i in range(1, rows + 1):
#     for j in range(rows-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="")
#     print()

# n = 6
# for i in range(1, n+1):
#     print("*" * i)
#
# n = 6
# for i in range(1, n+1):
#     print(" " * (n-i) + "*" * i)

# n = 6
# for i in range(n, 0, -1):
#     print("*" * i)
#
# n = 6
# for i in range(n, 0, -1):
#     print(" " * (n-i) + "*" * i)

n = 6
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)