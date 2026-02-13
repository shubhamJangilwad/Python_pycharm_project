import mysql.connector

conn = (mysql.connector.connect#connect ot mysql server
    (
    host="localhost",
    user="root",
    password="vishal@1234",
    database = "itshaala"
))
cursor = conn.cursor() # cursor is used to run sql commands
cursor.execute("DELETE FROM branch WHERE id = 7")
print("Deleted")
conn.commit()
conn.close()