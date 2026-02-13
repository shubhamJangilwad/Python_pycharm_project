import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user= "root",
    password="vishal@1234",
    database= "student_portal"
)
print("connection successfully")

cursor = conn.cursor()
username = input("Enter username : ")
password = input("Enter password : ")
full_name = input("Enter full_name : ")
course   = input("Enter course_name : ")
sql = "INSERT INTO students (username,password,full_name,course)VALUES(%s,%s,%s,%s)"
values = (username,password,full_name,course)

cursor.execute(sql,values)
conn.commit()
print("registration successfully")
