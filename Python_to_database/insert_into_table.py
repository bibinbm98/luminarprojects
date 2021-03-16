import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin="mysql_native_password",
    database="mydb"

)
cursor=db.cursor()
sql="insert into employee values('emp01','bibin',56000,'developer')"
cursor.execute(sql)
db.commit()
db.close()
