import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin="mysql_native_password",
    database="mydb"
)
cursor = db.cursor()
file = open('demo', 'r')
for lines in file:
    data = lines.rstrip("\n").split(",")


    sql = "insert into fruits values(%s,%s)"

    cursor.execute(sql,data)
    db.commit()
db.close()
