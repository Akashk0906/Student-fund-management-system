import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="akash",database="akashdb")
mycursor = mydb.cursor()
mycursor.execute("Create table student(name varchar(200),amt int(20))")
