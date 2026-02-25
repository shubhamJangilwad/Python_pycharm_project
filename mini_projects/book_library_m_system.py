import pickle
import os

file_name = "book.dat"
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

def add_book():
    data = load_data()
    book_name = input("Enter book name: ")
    author = input("Enter author name: ")
    book_price = int(input("Enter the price: "))

    book_entry = {
        "book_name": book_name,
        "author" : author,
        "book_price" : book_price
    }

    for book in data:
        if book["book_name"] == book_name:
            print("file already exist")
        return

    data.append(book_entry)
    save_data(data)
    print("book_entry successful")

def view_book():
    data = load_data()
    book_name = input("Enter book name: ")
    for book in data:
        if book["book_name"] == book_name:
            print(book)
        return
    print("book not found")

def search_book():
    data = load_data()
    book_name = input("Enter book name")
    for book in data:
        if book["book_name"] == book_name:
            print(book)
            return

    print("book not found")

def delete_book():
    data = load_data()
    book_name = input("Enter book name: ")
    for book in data:
        if book["book_name"] == book_name:
            data.remove(book)
            save_data(data)
            print("book deleted successfully")
            return
    print("book not found")

def update_price():
    data = load_data()
    book_name = input("Enter book name: ")
    new_price = int(input("Enter new price"))

    for book in data:
        if book["book_name"] == book_name:
            book["book_price"] = new_price
            save_data(data)
            print("book price updated")
            return
    print("book not found")

while True:

    print("1. Add book")
    print("2. View book")
    print("3. Search book")
    print("4. Update price")
    print("5. Delete book ")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_book()

    elif choice == "3":
        search_book()

    elif choice == "4":
        update_price()

    elif choice == "5":
        delete_book()

    elif choice == "6":
        print("Exiting program....")
        break

    else:
        print("Invalid choice")