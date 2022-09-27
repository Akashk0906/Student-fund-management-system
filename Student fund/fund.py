#--------------------------------------------------------------------------------------------------------------------------------
#******************************************THIS IS STUDENT FUND MANAGEMENT SYSTEM************************************************ 
#--------------------------------------------------------------------------------------------------------------------------------
#*****************************************************Import packages************************************************************
#--------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
import tkinter as tk
import mysql.connector
#--------------------------------------------------------------------------------------------------------------------------------
#*******************************************Take user id and password  from database*********************************************
#--------------------------------------------------------------------------------------------------------------------------------

mydb=mysql.connector.connect(host="localhost",user="root",password="akash",database="akash")
mycursor=mydb.cursor()

#Take user id from database
mycursor.execute("select userid from userpassword")
myresult=mycursor.fetchone()
for row in myresult:
    uid1=row

#Take password from database
mycursor.execute("select pass from userpassword")
result=mycursor.fetchone()
for row in result:
    pas1=row

#Take amount from database
mycursor.execute("select amount from userpassword")
result=mycursor.fetchone()
for row in result:
    amt1=row

#--------------------------------------------------------------------------------------------------------------------------------
#************************************************To check list of students*******************************************************
#--------------------------------------------------------------------------------------------------------------------------------
def check_l():
    #There I am using try except block to error handeling
    try:
        userid=usid.get()
        userpass=uspass.get()
        useryear=usyear.get()
        usersem=ussem.get()

        #Check all required information filled or not by user
        if(userid==""):
            messagebox.showerror("Stop!","Enter user id")
        elif(userpass==0):
            messagebox.showerror("Stop!","Enter password")
        elif(useryear==""):
            messagebox.showerror("Stop!","Enter year")
        elif(usersem==""):
            messagebox.showerror("Stop!","Enter semester")
        else:
            if(userid!=uid1):
                messagebox.showerror("Stop!","Enter correct user ID")
            elif(userpass!=pas1):
                messagebox.showerror("Stop!","Enter correct password")
            else:
                #Make a new GUI window to show table
                ak=tk.Tk()
                ak.geometry("340x800")
                ak.title("List of student")
                global i
                #here we connect to database and print the table
                mydb=mysql.connector.connect(host="localhost",user="root",password="akash",database="db"+useryear)
                mycursor=mydb.cursor()
                mycursor.execute("select * from {}".format(usersem))
                i=0
                for row in mycursor.fetchall():
                    for j in range(len(row)):
                        e=Label(ak,width=15,fg="blue",text=row[j],relief="ridge",anchor="w")
                        e.grid(row=i,column=j)
                    i=i+1
                ak.mainloop()
    except:
        messagebox.showwarning("Stop!","Enter integer value in password")
#--------------------------------------------------------------------------------------------------------------------------------
def check_list():
    global usid,uspass,usyear,ussem

    #Making basic window
    cl=tk.Tk()
    cl.title("Check List")
    cl.geometry("400x400")
    cl.resizable(False,False)

    #Make label in GUI
    Label(cl,text="Check List",font="algerian 20 bold",bg="red",fg="white").pack(fill="both")
    Label(cl,text="User ID",font="20").place(x=40,y=70)
    Label(cl,text="Password",font="20").place(x=40,y=110)
    Label(cl,text="Year",font="20").place(x=40,y=150)
    Label(cl,text="Semester",font="20").place(x=40,y=190)
    
    #Make boxes to take input
    usid=tk.StringVar(cl)
    uid=Entry(cl,font="10",bd=4,textvariable=usid)
    uid.place(x=140,y=70)
    uspass=tk.IntVar(cl)
    pas=Entry(cl,font="10",bd=4,textvariable=uspass)
    pas.place(x=140,y=110)
    OptionList2=[
        "",
    "2022"
    ]
    usyear=tk.StringVar(cl)
    usyear.set(OptionList2[0])
    year=tk.OptionMenu(cl,usyear,*OptionList2)
    year.config( font=("Helvetica",10))
    year.place(x=140,y=150)

    OptionList=[
    "",
    "sem1",
    "sem2",
    "sem3",
    "sem4",
    "sem5",
    "sem6"
    ]
    ussem=tk.StringVar(cl)
    ussem.set(OptionList[0])
    opt=tk.OptionMenu(cl,ussem,*OptionList)
    opt.config( font=("Helvetica",10))
    opt.place(x=140,y=190)
    #Check Button
    Button(cl,text="Check",font="20",bd=8,command=check_l).place(x=240,y=290)

    #Make function to reset the values
    def open():
        uspass.set(0)
        usyear.set("")
        ussem.set("")
        usid.set("")
    #Reset button
    Button(cl,text=" Reset",font="20",bd=8,command=open).place(x=70,y=290)
    cl.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------
#********************************************To check amount of particular student***********************************************
#--------------------------------------------------------------------------------------------------------------------------------
def check_a():
    #There I am using try except block to error handeling
    try:
        uroll=sroll.get()
        uyear=syear.get()
        usem=ssem.get()
        if(uroll==0):
            messagebox.showerror("Stop!","Please enter your rollno.")
        elif(uyear==""):
            messagebox.showerror("Stop!","Please select year")
        elif(usem==""):
            messagebox.showerror("Stop!","Please select semester")
        else:
            #Here we fetch data from database of a particular student
            mydb=mysql.connector.connect(host="localhost",user="root",password="akash",database="db"+uyear)
            mycursor=mydb.cursor()
            mycursor.execute("select amount from {} where rollno={}".format(usem,uroll))
            for row in mycursor.fetchone():
                t=row
            messagebox.showinfo("You deposited...",t)
    except:
        messagebox.showwarning("Stop","Enter only integer value in roll no.")
#--------------------------------------------------------------------------------------------------------------------------------
def check_amount():
    #Define global variable
    global syear,ssem,sroll
    ca=tk.Tk()
    ca.title("Check amount")
    ca.geometry("400x400")
    ca.resizable(False,False)
    Label(ca,text="Check Amount",font="algerian 20 bold",bg="red",fg="white").pack(fill="both")
    
    #Label define
    Label(ca,text="Roll no.",font="20").place(x=40,y=70)
    Label(ca,text="Year",font="20").place(x=40,y=110)
    Label(ca,text="Semester",font="20").place(x=40,y=150)
    
    # Text Box
    sroll=tk.IntVar(ca)
    roll=Entry(ca,font="10",bd=4,textvariable=sroll)
    roll.place(x=140,y=70)
    
    OptionList2=[
        "",
    "2022"
    ]
    syear=tk.StringVar(ca)
    syear.set(OptionList2[0])
    year=tk.OptionMenu(ca,syear,*OptionList2)
    year.config( font=("Helvetica",10))
    year.place(x=140,y=110)

    OptionList=[
    "",
    "sem1",
    "sem2",
    "sem3",
    "sem4",
    "sem5",
    "sem6"
    ]
    ssem=tk.StringVar(ca)
    ssem.set(OptionList[0])
    opt=tk.OptionMenu(ca,ssem,*OptionList)
    opt.config( font=("Helvetica",10))
    opt.place(x=140,y=150)
  
    #buttons
    Button(ca,text="Submit",font="20",bd=8,command=check_a).place(x=240,y=270)
    def open():
        sroll.set(0)
        syear.set("")
        ssem.set("")
    Button(ca,text=" Reset",font="20",bd=8,command=open).place(x=70,y=270)
    ca.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------
#*************************************************To check balance in fund*******************************************************
#--------------------------------------------------------------------------------------------------------------------------------
def check_b():
    #There I am using try except block to error handeling
    try:
        userid=uuid.get()
        userpas=upas.get()
        if(userid==""):
            messagebox.showerror("Stop!","Please enter your user ID")
        elif(userpas==0):
            messagebox.showerror("Stop!","Please enter password")
        else:
            if(userid!=uid1):
                messagebox.showerror("Stop!","Wrong user ID")
            elif(userpas!=pas1):
                messagebox.showerror("Stop!","Wrong password")
            else:
                tk.messagebox.showinfo("Your balance...",amt1)
    except:
        messagebox.showwarning("Stop!","Enter only integer value in password")
#--------------------------------------------------------------------------------------------------------------------------------
def check_balance():
    #Define global variabe
    global uuid,upas

    #Make basic GUI window
    ch=tk.Tk()
    ch.title("Check Balance")
    ch.geometry("400x300")
    ch.resizable(False,False)

    #make labels
    Label(ch,text="Check Balance",font="algerian 20 bold",bg="red",fg="white").pack(fill="both")
    Label(ch,text="User ID",font="20").place(x=40,y=70)
    Label(ch,text="Password",font="20").place(x=40,y=110)
    uuid=tk.StringVar(ch)
    uid=Entry(ch,font="10",bd=4,textvariable=uuid)
    uid.place(x=140,y=70)
    upas=tk.IntVar(ch)
    pas=Entry(ch,font="10",bd=4,textvariable=upas)
    pas.place(x=140,y=110)

    # Make Buttons
    Button(ch,text="Check",font="20",bd=8,command=check_b).place(x=240,y=190)
    def open():
        uuid.set("")
        upas.set(0)
    Button(ch,text=" Reset",font="20",bd=8,command=open).place(x=70,y=190)
    ch.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------
#***************************************************About the student fund*******************************************************
#--------------------------------------------------------------------------------------------------------------------------------
def about():
    abu=Tk()
    abu.geometry("850x320")
    abu.title("About")
    #Here we give message about student fund management
    ak=Label(abu,text='''This fund management system make to help the other students and for 
oraganising the function. If you are interested then submit some amount

This fund management system made by:
 Akash Kushwaha
 Akash Kosta
 Abhishek Singh
 Anupam Upadhyay
 Abhay Yadav
 Abhay Pratap Singh ''',bg="black",fg="white",font="comicsansms 19 italic",borderwidth=20,relief=SUNKEN)
    ak.pack()                 
    abu.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------
#*******************************************************To deposit the amount****************************************************
#--------------------------------------------------------------------------------------------------------------------------------
def deposit():
    #There I am using try except block to error handeling
    try:
        username = tname.get()
        userroll = troll.get()
        useryear = v.get()
        usersem = va.get()
        useramt = tamt.get()

        #Check the entries whether it is filled or not
        if(username==""):
            messagebox.showerror("Stop!","Please enter your name")
        elif(userroll==0):
            messagebox.showerror("Stop!","Please enter your Roll no.")
        elif(useryear==""):
            messagebox.showerror("Stop!","Please select your year")
        elif(usersem==""):
            messagebox.showerror("Stop!","Please select your semester")
        elif(useramt==0):
            messagebox.showerror("Stop!","Please enter your amount")
        else:
            #Connect to database and update values
            db="db"+useryear
            yourdb = mysql.connector.connect(host="localhost",user="root",passwd="akash",database=db)
            mycursor=yourdb.cursor()
            sqlform="insert into {}(rollno,name,amount) values({},'{}',{})".format(usersem,userroll,username,useramt)
            mycursor.execute(sqlform)
            yourdb.commit()
            ydb = mysql.connector.connect(host="localhost",user="root",passwd="akash",database="akash")
            ycursor=ydb.cursor()
            a=amt1+useramt
            sql="UPDATE userpassword SET amount={} WHERE userid='fund2022'".format(a)
            ycursor.execute(sql)
            ydb.commit()
            messagebox.showinfo("Welcome...","Fund Deposited")
    except:
        messagebox.showwarning("Stop!","Enter integer value in rollno,amount and number is not start with 0")
#--------------------------------------------------------------------------------------------------------------------------------
def deposit_fund():
    global tname,troll,v,va,tamt
    ak=tk.Tk()
    ak.title("Deposit fund")
    ak.geometry("400x400")
    ak.resizable(False,False)
    Label(ak,text="Deposit Fund",font="algerian 20 bold",bg="red",fg="white").pack(fill="both")
    
    #Label define
    Label(ak,text="Name",font="20").place(x=40,y=70)
    Label(ak,text="Roll no.",font="20").place(x=40,y=110)
    Label(ak,text="Year",font="20").place(x=40,y=150)
    Label(ak,text="Semester",font="20").place(x=40,y=190)
    Label(ak,text="Amount",font="20").place(x=40,y=230)
    
    # Text Box
    tname=tk.StringVar(ak)
    name=Entry(ak,font="10",bd=4,textvariable=tname)
    name.place(x=140,y=70)
    troll=tk.IntVar(ak)
    roll=Entry(ak,font="10",bd=4,textvariable=troll)
    roll.place(x=140,y=110)
    
    OptionList2=[
        "",
    "2022"
    ]
    v=tk.StringVar(ak)
    v.set(OptionList2[0])
    year=tk.OptionMenu(ak,v,*OptionList2)
    year.config( font=("Helvetica",10))
    year.place(x=140,y=150)

    OptionList=[
    "",
    "sem1",
    "sem2",
    "sem3",
    "sem4",
    "sem5",
    "sem6"
    ]
    va=tk.StringVar(ak)
    va.set(OptionList[0])
    opt=tk.OptionMenu(ak,va,*OptionList)
    opt.config( font=("Helvetica",10))
    opt.place(x=140,y=190)

    tamt=tk.IntVar(ak)
    amt=Entry(ak,font="10",bd=4,textvariable=tamt)
    amt.place(x=140,y=230)
  
    #button
    Button(ak,text="Deposit",font="20",bd=8,command=deposit).place(x=240,y=310)
    def open():
        tamt.set(0)
        v.set("")
        va.set("")
        tname.set("")
        troll.set(0)
    Button(ak,text=" Reset ",font="20",bd=8,command=open).place(x=70,y=310)
    ak.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------
#**************************************************To withdraw the amount********************************************************
#--------------------------------------------------------------------------------------------------------------------------------
def withdraw():
    #There I am using try except block to error handeling
    try:
        userid = tuid.get()
        userpas = tpas.get()
        useramt = tamot.get()
        if(userid==""):
            messagebox.showerror("Stop!","Please enter your user ID")
        elif(userpas==0):
            messagebox.showerror("Stop!","Please enter your password")
        elif(useramt==0):
            messagebox.showerror("Stop!","Please enter your amount")
        else:
            if(userid!=uid1):
                messagebox.showerror("Stop!","Wrong User ID")
            elif(userpas!=pas1):
                messagebox.showerror("Stop!","Wrong password")
            else:
                if(amt1>=useramt):
                    ydb = mysql.connector.connect(host="localhost",user="root",passwd="akash",database="akash")
                    ycursor=ydb.cursor()
                    a=amt1-useramt
                    sql="UPDATE userpassword SET amount={} WHERE userid='fund2022'".format(a)
                    ycursor.execute(sql)
                    ydb.commit()
                    messagebox.showinfo("welcome...","withdrawal success")
                else:
                    messagebox.showerror("Stop!","Not sufficient balance")
    except:
        messagebox.showwarning("Stop!","Enter integer value in password and amount")
#--------------------------------------------------------------------------------------------------------------------------------
def withdraw_fund():
    #Here we define global variable
    global tuid,tpas,tamot

    #Make basic GUI
    ab=tk.Tk()
    ab.title("Withdraw fund")
    ab.geometry("400x300")
    ab.resizable(False,False)

    #Make labels
    Label(ab,text="Withdraw Fund",font="algerian 20 bold",bg="red",fg="white").pack(fill="both")
    Label(ab,text="User ID",font="20").place(x=40,y=70)
    Label(ab,text="Password",font="20").place(x=40,y=110)
    Label(ab,text="Amount",font="20").place(x=40,y=150)

    #Make entry boxes
    tuid=tk.StringVar(ab)
    uid=Entry(ab,font="10",bd=4,textvariable=tuid)
    uid.place(x=140,y=70)
    tpas=tk.IntVar(ab)
    pas=Entry(ab,font="10",bd=4,textvariable=tpas)
    pas.place(x=140,y=110)
    tamot=tk.IntVar(ab)
    amt=Entry(ab,font="10",bd=4,textvariable=tamot)
    amt.place(x=140,y=150)
    
    #Buttons
    Button(ab,text="Withdraw",font="20",bd=8,command=withdraw).place(x=240,y=230)
    def open():
        tamot.set(0)
        tuid.set("")
        tpas.set(0)
    Button(ab,text=" Reset  ",font="20",bd=8,command=open).place(x=70,y=230)
    ab.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------
#**************************************************Main GUI function*************************************************************
#--------------------------------------------------------------------------------------------------------------------------------

#Define object
root = Tk()
photo=PhotoImage(file="ic.png")
root.iconphoto(False,photo)
root.title("Student Fund Management")
root.geometry("1400x800")
root.minsize(800,800)
root.maxsize(1920,1080)

#Menu bar
mymenu=Menu(root)
m1=Menu(mymenu)
m1.add_command(label="Check balance",command=check_balance)
m1.add_command(label="check amount of student",command=check_amount)
m1.add_command(label="About",command=about)
m1.add_command(label="Check list",command=check_list)
root.config(menu=mymenu)
mymenu.add_cascade(label="Menu",menu=m1)
mymenu.add_cascade(label="Exit",command=quit)
myfile=Menu(root)

#import image
image=Image.open("frontpg.jpg")
photo=ImageTk.PhotoImage(image)
label=Label(image=photo)
label.pack()

#Label defined which is shown in display
Label(text="                                                Dr. VIRENDRA SWARUP INSTITUTE OF COMPUTER STUDIES                                                   ",font="algerian 20 bold",bg="navy blue",fg="white").place(x=0,y=0)
Label(text="STUDENT",font="algerian 40 bold",bg="orange").place(x=200,y=150)
Label(text="FUND",font="algerian 20 bold",bg="orange").place(x=280,y=235)
Label(text="MANAGEMENT",font="algerian 40 bold",bg="orange").place(x=135,y=290)

#Buttons of deposit and withdraw
Button(text=" DEPOSIT FUND",font="bold",bd=10,bg="sky blue",fg="black",command=deposit_fund).place(x=100,y=500)
Button(text="WITHDRAW FUND",font="bold",bd=10,bg="sky blue",fg="black",command=withdraw_fund).place(x=350,y=500)
root.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------
#*******************************************************THE END******************************************************************
#--------------------------------------------------------------------------------------------------------------------------------
