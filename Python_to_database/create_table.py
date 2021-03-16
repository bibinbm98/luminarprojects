import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin="mysql_native_password",
    database="mydb"

)
cursor=db.cursor()
sql="create table employee(eid varchar(20),name varchar(20),salary int,desig varchar(50))"
cursor.execute(sql)
print("TABLE CREATED")