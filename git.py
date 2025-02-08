#code for MySQL

import mysql.connector

a = mysql.connector.connect(host = "localhost", user = "root", passwd = "AEISEClog@123", database = "sharma1")


mycursor = a.cursor()
mycursor.execute("select * from Student")

result = mycursor.fetchall()

for i in result:
    print(i)    
