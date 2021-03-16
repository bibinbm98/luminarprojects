import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin="mysql_native_password",
    database="mydb"

)
cursor=db.cursor()
sql="select * from employee"

cursor.execute(sql)
data=cursor.fetchall()
print(data)
db.close()