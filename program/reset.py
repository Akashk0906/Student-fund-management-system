from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
import tkinter as tk
import mysql.connector
def check_b():
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
         
            

def check_balance():
    global uuid,upas
    ch=tk.Tk()
    ch.title("Check Balance")
    ch.geometry("400x300")
    ch.resizable(False,False)
    Label(ch,text="Check Balance",font="algerian 20 bold",bg="red",fg="white").pack(fill="both")
    Label(ch,text="User ID",font="20").place(x=40,y=70)
    Label(ch,text="Password",font="20").place(x=40,y=110)
    uuid=tk.StringVar(ch)
    uid=Entry(ch,font="10",bd=4,textvariable=uuid)
    uid.place(x=140,y=70)
    upas=tk.IntVar(ch)
    pas=Entry(ch,font="10",bd=4,textvariable=upas)
    pas.place(x=140,y=110)
    Button(ch,text="Check",font="20",bd=8,command=check_b).place(x=240,y=190)
    def open():
        uuid.set("")
        upas.set(0)
    Button(ch,text="reset",font="20",bd=8,command=open).place(x=70,y=190)
    ch.mainloop()
    
check_balance()