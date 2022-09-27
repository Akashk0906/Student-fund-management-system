from  tkinter import*
from tkinter import messagebox
def register():
    username=name.get()
    useremail=email.get()
    userphone=phone.get()
    usercity=city.get()
    if(username==""):
        messagebox.showerror("stop !", "please enter your name")
        if(useremail==""):
            messagebox.showerror("stop !","please enter your email")
        elif(userphone==""):
            messagebox.showerror("stop !","please enter your phone")
        elif(usercity==""):
            messagebox.showerror("stop !","please enter your city")
        else:
            messagebox.showerror("welcome","thanks for registration !!")

screen=Tk()
#widget or components
Label(screen,text="registration form",font="ariel 20 bold", bg="red",fg="white").pack(fill="both")
screen.title("registration")
screen.geometry("500x500")
screen.resizable(False,False)
#Label
Label(screen,text="Name",font="10",fg="black").place(x=110,y=90)
Label(screen,text="Email",font="10",fg="black").place(x=110,y=140)
Label(screen,text="Phone",font="10",fg="black").place(x=110,y=190)
Label(screen,text="City",font="10",fg="black").place(x=110,y=240)
#textbox
tname=StringVar()
temail=StringVar()
tphone=StringVar()
tcity=StringVar()

name=Entry(screen,bd=6,textvariable="tname")
name.place(x=320,y=90)
email=Entry(screen,bd=6,textvariable="temail")
email.place(x=320,y=140)
phone=Entry(screen,bd=6,textvariable="tphone")
phone.place(x=320,y=190)
city=Entry(screen,bd=6,textvariable="tcity")
city.place(x=320,y=240)
screen.mainloop()        
