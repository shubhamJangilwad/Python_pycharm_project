import mysql.connector


conn = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "vishal@1234",
    database = "itshaala"

)
print("Connected successfully")

cursor = conn.cursor()#cursor is used to run SQL commands
sql = "INSERT INTO branch(id,name,address)VALUES(%s,%s,%s)"
values = [
    (7,"Mern","Pune"),
    (8,"data_analytics","Pune"),
    (9,"Data science","Pune"),
    (10,"data analysis","Pune")
]
cursor.executemany(sql,values)
print("data inserted")
conn.commit()

cursor.execute( "SELECT * FROM branch")
result = cursor.fetchall()
print("show data of table")
for i in result:
    print(i)
conn.close()
