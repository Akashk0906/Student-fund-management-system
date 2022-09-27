from tkinter import *
ak=Tk()
ak.title("Registratuon form")
ak.geometry("400x400")
ak.resizable(False,False)
Label(ak,text="Registration form",font="arial 20 bold",bg="red",fg="white").pack(fill="both")
#Label define
Label(ak,text="Name",font="20").place(x=40,y=70)
Label(ak,text="Email",font="20").place(x=40,y=110)
# Text Box
name=Entry(ak,font="10",bd=4)
name.place(x=140,y=70)
email=Entry(ak,font="10",bd=4)
email.place(x=140,y=110)
#button
Button(ak,text="Register",font="20").place(x=240,y=190)
ak.mainloop()