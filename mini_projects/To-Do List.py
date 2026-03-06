to_do = []

while True:
    print("1 : Add Task")
    print("2 : View Task")
    print("3 : Delete Task")
    print("4 : Exit")

    user = int(input("Enter choice: "))

    if user == 1:
        to_do.append(input("Enter the task: "))
    elif user == 2:
        for i in range(len(to_do)):
            print(i+1,to_do[i])
    elif user == 3:
        to_do.pop(int(input("Enter the task: ")))
    elif user == 4:
        print("Exit the program")
        break

