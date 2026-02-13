import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "vishal@1234",
    database = "student_portal"
)

cursor = conn.cursor()
email = input("Enter the email :")
address = input("Enter the address :")
id = input("Enter the id :")
sql = "UPDATE students SET email =%s , address = %s WHERE id = %s"
values = (email,address,id)
cursor.execute(sql,values)
conn.commit()
conn.close()
