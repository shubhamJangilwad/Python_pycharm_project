import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'vishal@1234',
    database = "laptop"
)

print("connections successfully")

cursor = conn.cursor()
def create_table():
    sql = input("Enter a CREATE TABLE query: ")
    cursor.execute(sql)
    conn.commit()
    print("table created successfully")

def insert_values():
    laptop_name = input("Enter the laptop_name:")
    price = int(input("Enter the laptop_price:"))
    sql = "INSERT INTO laptop(laptop_name,price)VALUES(%s,%s)"
    values = (laptop_name,price)
    cursor.execute(sql,values)
    conn.commit()
    print("values are inserted")


def update_price():
    id = int(input("Enter the laptop_id: "))

    print("1 : update lap_name")
    print("2 : update lap_price")

    choice = int(input("Enter a choice: "))

    if choice == 1:
        laptop_name = input("Enter lap_new_name:")
        sql = "UPDATE laptop SET laptop_name = %s WHERE id = %s"
        values = (laptop_name , id)
    elif choice == 2:
        price = int(input("Enter lap_new_price:"))
        sql = "UPDATE laptop SET price = %s WHERE id = %s"
        values = (price, id)

    else:
        print("invalid choice")
        return

    cursor.execute(sql,values)
    print("values updated successfully")


def delete_values():
    laptop_id = int(input("Enter the lap_id: "))

    sql_check = "SELECT * FROM laptop WHERE id = %s"
    cursor.execute(sql_check, (laptop_id,))
    result = cursor.fetchone()

    if result:
        sql_delete = "DELETE FROM laptop WHERE id = %s"
        cursor.execute(sql_delete, (laptop_id,))
        conn.commit()

        print("Successfully deleted the row")
    else:
        print("id not found")

def show():
    laptop_id = int(input("Enter the lap_id :"))
    sql_check = "SELECT * FROM laptop WHERE id = %s"
    cursor.execute(sql_check,(laptop_id,))
    result = cursor.fetchone()

    if result:
        print(result)
    else:
        print("id not found")

while True:
    print("1 : create table")
    print("2 : insert values")
    print("3 : update values")
    print("4 : delete values")
    print("5: show data")
    print("6 : exit")

    choice = input("Enter choice: ")
    if choice == "1":
        create_table()
    elif choice == "2":
        insert_values()
    elif choice == "3":
        update_price()
    elif choice == "4":
        delete_values()
    elif choice == "5":
        show()
    elif choice == "6":
        print("exit....")
        break
    else:
        print("invalid choice")

conn.close()