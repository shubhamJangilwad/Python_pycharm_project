import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user= "root",
    password="vishal@1234",
    database= "student_portal"
)
print("connection successfully")

cursor = conn.cursor()
username = input("Enter username: ")
password = input("Enter password: ")

sql = "SELECT * FROM students WHERE username = %s AND password = %s"
values = (username, password)

cursor.execute(sql, values)

result = cursor.fetchone()

if result:
    print("Login successful")
else:
    print("Invalid username or password")

print("Welcome", result[3])
print("Course:", result[4])
