contact = {}

while True:
    print("\n1: Add Contact")
    print("2 : View Contact")
    print("3 : Search Contact")
    print("4 : Delete Contact")
    print("5: Exit")

    user = int(input("Enter choice: "))

    if user == 1:
        contact_name = input("Enter contact name: ")
        phone_num = int(input("Enter phone number: "))
        if len(str(phone_num))!=10:
            print("invalid phone number")
        if contact_name not in contact:
            contact[contact_name] = phone_num
            print("successfully added")

    elif user == 2:
        for name , number in contact.items():
            print(name ,":",number)

    elif user == 3:
        search_num = input("Enter name: ")
        if search_num in contact:
            print(contact[search_num])
        else:
            print("invalid name")

    elif user == 4:
        delete_contact = input("Enter contact name: ")

        if delete_contact in contact:
            del contact[delete_contact]
            print("successfully deleted the contact")
        else:
            print("invalid contact name")

    elif user == 5:
        print("Exit the program")
        break

