import pickle
import os

file_name = "employees.dat"

if not os.path.exists(file_name):
    with open(file_name, "wb") as f:
        pickle.dump([], f)


def load_data():
    with open(file_name,"rb") as f:
        data = pickle.load(f)
        return data

def save_data(data):
    with open(file_name,"wb") as f:
        pickle.dump(data,f)


def add_employee():
    data = load_data()
    emp_id = int(input("Enter a id: "))
    name = input("Enter the name: ")
    salary = int(input("Enter salary: "))
    department = input("Enter department: ")

    employee = {
        "emp_id" : emp_id,
        "name" : name,
        "salary" : salary,
        "department": department

    }

    for emp in data:
        if emp["emp_id"] == emp_id:
            print("Already exists")
            return

    data.append(employee)
    save_data(data)
    print("Employee added successfully")



def view_employee():
    data = load_data()
    if not data:
        print("No employees found")

    else:
        for i in data:
            print(i)

def search_employee():
    data = load_data()
    emp_id = int(input("Enter emp_id: "))

    for emp in data:
        if emp["emp_id"] == emp_id:
            print(emp)
            return

    print("Employee not found")

def delete_employee():
    data = load_data()
    emp_id = int(input("Enter emp_id: "))
    for emp in data:
        if emp["emp_id"] == emp_id:
            data.remove(emp)
            save_data(data)
            print("Employee deleted successfully")
            return
    print("Employee not found")


def update_salary():
    data = load_data()
    emp_id = int(input("Enter emp_id : "))
    new_salary = int(input("Enter salary: "))
    for emp in data:
        if emp["emp_id"] == emp_id:
            emp["salary"] = new_salary
            save_data(data)
            print("Updated the salary")
            return
    print("Employee not found")

while True:

    print("1. Add employee")
    print("2. View employee")
    print("3. Search employee")
    print("4. Update salary")
    print("5. Delete employee ")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employee()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_salary()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        print("Exiting program....")
        break

    else:
        print("Invalid choice")
