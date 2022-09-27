import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="akash",database="db2022")
mycursor=mydb.cursor()
a='sem4'
b=50
mycursor.execute("select amount from {} where rollno={}".format(a,b))
for row in mycursor.fetchone():
    t=row
print(t)
'''
mycursor.execute("insert into userpassword(userid,pass,amount) values('fund2022',20222022,0)")
mydb.commit()
##################################
mycursor.execute("select username from pass")
myresult=mycursor.fetchone()
for row in myresult:
    uid1=row
mycursor.execute("select pass from pass")
result=mycursor.fetchone()
for row in result:
    pas1=row
mycursor.execute("select amount from pass")
yresult=mycursor.fetchall()
for row in yresult:
    prtint(row)
#enter the values
sqlform="Insert into pass(amount) values(0)" 
mycursor.execute(sqlform)
mydb.commit()
'''
