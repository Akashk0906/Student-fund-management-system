from tkinter import *
import tkinter as tk
from tkinter import messagebox

def deposit():
    username = tname.get()
    userroll = troll.get()
    useryear = v.get()
    usersem = va.get()
    useramt = tamt.get()
    if(username==""):
        messagebox.showerror("Stop!","Please enter your name")
    elif(userroll==""):
        messagebox.showerror("Stop!","Please enter your Roll no.")
    elif(useryear==""):
        messagebox.showerror("Stop!","Please select your year")
    elif(usersem==""):
        messagebox.showerror("Stop!","Please select your semester")
    elif(useramt==""):
        messagebox.showerror("Stop!","Please enter your amount")
    else:
        print(username)
        print(userroll)
        print(useryear)
        print(usersem)
        print(useramt)
        messagebox.showinfo("Welcome...","Fund Deposited")


def deposit_fund():

    global tname,troll,v,va,tamt
    ak=tk.Tk()
    tname=StringVar()
    troll=StringVar()
    v=StringVar()
    va=StringVar()
    tamt=StringVar()
    ak.title("Deposit fund")
    ak.geometry("400x400")
    ak.resizable(False,False)
    Label(ak,text="Deposit Fund",font="arial 20 bold",bg="red",fg="white").pack(fill="both")
    #Label define
    Label(ak,text="Name",font="20").place(x=40,y=70)
    Label(ak,text="Roll no.",font="20").place(x=40,y=110)
    Label(ak,text="Year",font="20").place(x=40,y=150)
    Label(ak,text="Semester",font="20").place(x=40,y=190)
    Label(ak,text="Amount",font="20").place(x=40,y=230)
    # Text Box
    
    name=Entry(ak,font="10",bd=4,textvariable=tname)
    name.place(x=140,y=70)
    roll=Entry(ak,font="10",bd=4,textvariable=troll)
    roll.place(x=140,y=110)
    
    OptionList2=[
        "select",
    "2022"
    ]
    v=tk.StringVar(ak)
    v.set(OptionList2[0])
    year=tk.OptionMenu(ak,v,*OptionList2)
    year.config( font=("Helvetica",10))
    year.place(x=140,y=150)

    OptionList=[
    "select",
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

    amt=Entry(ak,font="10",bd=4,textvariable=tamt)
    amt.place(x=140,y=230)
  
    #button
    Button(ak,text="Deposit",font="20",bd=8,command=deposit).place(x=240,y=310)
    ak.mainloop()
deposit_fund()