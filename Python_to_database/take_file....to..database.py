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
    data = lines.rstrip("\n")
    lst = data.split(",")
    print(lst)
    sql = "insert into fruits values(%s,%s)"
    record = (lst[0], lst[1])
    cursor.execute(sql, record)
    db.commit()
db.close()
