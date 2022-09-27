import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="akash",database="ticket")
mycursor=mydb.cursor()
name=input()
adno=input()
tname=name+adno
mycursor.execute("CREATE TABLE {}(date VARCHAR(8),time VARCHAR(8),credit int,debit int)".format(tname))
print("table created")