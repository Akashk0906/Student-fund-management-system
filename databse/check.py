from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
import tkinter as tk
import mysql.connector
s='sem4'
a="2022"
ak=tk.Tk()
ak.geometry("170x800")
global i
mydb=mysql.connector.connect(host="localhost",user="root",password="akash",database="db"+a)
mycursor=mydb.cursor()
mycursor.execute("select * from {}".format(s))
i=0
for row in mycursor.fetchall():
    for j in range(len(row)):
        pass
        e=Label(ak,width=8,fg="blue",text=row[j],relief="ridge",anchor="w")
        e.grid(row=i,column=j)
    i=i+1
ak.mainloop()

