import pickle
import os

file_name = "students.dat"

# create file if not exists
if not os.path.exists(file_name):
    with open(file_name, "wb") as f:
        pickle.dump([], f)



# Load data from file
def load_data():
    with open(file_name, "rb") as f:
        return pickle.load(f)


# Save data to file
def save_data(data):
    with open(file_name, "wb") as f:
        pickle.dump(data, f)


# Add student
def add_student():
    data = load_data()

    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }

    data.append(student)
    save_data(data)

    print("Student Added Successfully!")


# View students
def view_students():
    data = load_data()

    if not data:
        print("No records found.")
    else:
        for student in data:
            print(student)


# Search student
def search_student():
    data = load_data()
    roll = int(input("Enter Roll Number to search: "))

    for student in data:
        if student["roll"] == roll:
            print("Student Found:", student)
            return

    print("Student not found.")


# Delete student
def delete_student():
    data = load_data()
    roll = int(input("Enter Roll Number to delete: "))

    for student in data:
        if student["roll"] == roll:
            data.remove(student)
            save_data(data)
            print("Student Deleted Successfully!")
            return

    print("Student not found.")


# Menu
while True:
    print("\n===== Student Record Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice")