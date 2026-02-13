import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "vishal@1234",
    database = "itshaala"
)
print("connection successfully")
cursor = conn.cursor()
sql = "INSERT INTO hr (id, name ,Address ) VALUES(%s,%s,%s)"
values =[
    (1,"shubham","Pune"),
    (2,"hanumant","Parbhani"),
    (3,"rajjat","Wardha"),
    (4,"shantanu","Nagpur"),
    (5,"harshal","Nagpur")
]
cursor.executemany(sql,values)
conn.commit()
print("values inserted successfully")
conn.close()
