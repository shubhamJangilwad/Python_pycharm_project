import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vishal@1234"
)

print("Connected")

cursor = conn.cursor()

cursor.execute("CREATE DATABASE itshaala")

print("Database created")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vishal@1234",
    database="itshaala"
)

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    marks INT
)
""")

print("Table created")
