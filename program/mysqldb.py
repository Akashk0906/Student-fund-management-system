import mysql.connector
from tkinter import messagebox
db="db2022"
ydb = mysql.connector.connect(host="localhost",user="root",passwd="akash",database=db)
ycursor=ydb.cursor()
a=3300
sql="Select * from sem4"
ycursor.execute(sql)
for row in ycursor.fetchall():
    messagebox.showinfo("welcome..",row)


    

