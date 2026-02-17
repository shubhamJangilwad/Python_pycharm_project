import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "vishal@1234",
    database = "itshaala"
)
print("Connection Successfully")
cursor = conn.cursor()
sql = "UPDATE shubham1 SET name = %s WHERE id = %s"
values = ("Shantanu",9)
cursor.execute(sql,values)
print("values updated")
conn.commit()
conn.close()