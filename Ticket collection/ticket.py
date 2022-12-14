import qrcode
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as tmsg
from PIL import Image


# functions

root=Tk()
root.title("Bus Ticketing system By Nikhil Maurya")
root.geometry("1366x768")
root.config(bg="light blue")

def Register():
    user_qrcode=qrcode.make(str(var5.get())+"@"+str(var1.get()))
    user_qrcode.save(str(var1.get())+"qrcode.png")
    msg=tmsg.showinfo()
    img = Image. open(str(var1.get())+"qrcode.png")
    img. show()

var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
def New_passenger():
    f1=Frame(root,bg="light gray",height=600,width=580,relief=GROOVE,border=10)
    f1.place(x=400,y=50)

    l1=Label(f1,text="New Passenger Registration",font=("Lato",25),bg="light gray")
    l1.place(x=80,y=20)

    cross=Button(f1,text="X",command=f1.destroy)
    cross.place(x=540,y=1)

    l2=Label(f1,text="Name",font=("Lato",15),bg="light gray")
    l2.place(x=110,y=120)
    E2=Entry(f1,textvariable=var1,font=("Lato",15))
    E2.place(x=220,y=120)
    
   

    l3=Label(f1,text="Gender",font=("Lato",15),bg="light gray")
    l3.place(x=110,y=180)
    E3=Radiobutton(f1,text="Male",value=1,variable=var3,bg="lightGray")
    E3.place(x=220,y=180)
    E3=Radiobutton(f1,text="female",value=2,variable=var3,bg="lightGray")
    E3.place(x=280,y=180)
    E3=Radiobutton(f1,text="Not to Specify",value=3,variable=var3,bg="lightGray")
    E3.place(x=350,y=180)
    
    l4=Label(f1,text="Mobile NO.",font=("Lato",15),bg="light gray")
    l4.place(x=110,y=240)
    E4=Entry(f1,textvariable=var2,font=("Lato",15))
    E4.place(x=220,y=240)

    l5=Label(f1,text="EMAIL",font=("Lato",15),bg="light gray")
    l5.place(x=110,y=300)
    E5=Entry(f1,textvariable=var4,font=("Lato",15))
    E5.place(x=220,y=300)

    l6=Label(f1,text="ADDHAR",font=("Lato",15),bg="light gray")
    l6.place(x=110,y=360)
    E6=Entry(f1,textvariable=var5,font=("Lato",15))
    E6.place(x=220,y=360)

    l6=Label(f1,text="Passward",font=("Lato",15),bg="light gray")
    l6.place(x=110,y=420)
    E6=Entry(f1,textvariable=var6,font=("Lato",15))
    E6.place(x=220,y=420)

    b1=Button(f1,text="Register",font=("Leto",15),command=Register)
    b1.place(x=260,y=480)

    
def About():
    msg=tmsg.showinfo("About",''' This is an prototype for solving an real tym problem as discussed in Project portfolio that is we are going to sort problem of E-bus ticketing as we are in hurry so we had overcome the problem of paper ticketing we issue an QR code in whhich the  details of pasenger are encoded and entire process of ticketing done within few seconds ''')
def Contact():
    msg=tmsg.showinfo("Contact Details", '''Contact us at : \n

    Gmail : nikhil020105@gmail.com
    github : https://github.com/Nikhil-maurya-N
    Linkedin : https://www.linkedin.com/in/nikhil-maurya-13535320b
    Instagram : https://instagram.com/a_n_on_y_m_o_us_?igshid=YmMyMTA2M2Y=
    ''')
def Recharge():
    var6=StringVar()
    var7=StringVar()

    f2=Frame(root,bg="light gray",height=400,width=380,relief=GROOVE,border=10)
    f2.place(x=400,y=50)

    l_1=Label(f2,text="Passenger Recharge Interface ",font=("Lato",17),bg="light gray")
    l_1.place(x=30,y=30)

    l_2=Label(f2,text="Email",font=("Lato",13),bg="light gray")
    l_2.place(x=50,y=100)
    E_2=Entry(f2,textvariable=var6,font=("Lato",13))
    E_2.place(x=140,y=100)

    l_3=Label(f2,text="Passward",font=("Lato",13),bg="light gray")
    l_3.place(x=50,y=150)
    E_4=Entry(f2,textvariable=var7,font=("Lato",13,))
    E_4.place(x=140,y=150)

    c1=Checkbutton(f2,text="Ha Hm insaan h",bg="light gray")
    c1.place(x=120,y=200)

    b2=Button(f2,text="Log in",font=("Leto",13),command=log_in)
    b2.place(x=170,y=250)

def log_in():
    pass


def Exit():
    exit()
mainmenu=Menu(root)

# declartion of first menu named as m1(file)
m1=Menu(mainmenu,tearoff=0)
mainmenu.add_cascade(label="Passenger Adminitration",font=("BOLD",30),menu=m1)
m1.add_command(label="New Passenger...",font=("BOLD",15),command=New_passenger)
m1.add_command(label="Recharge",font=("BOLD",15),command=Recharge)
m1.add_command(label="About",font=("BOLD",15),command=About)
m1.add_command(label="Contact Us",font=("BOLD",15),command=Contact)
m1.add_command(label="De-Activation",font=("BOLD",15),command=None)
m1.add_command(label="Exit",font=("BOLD",15),command=Exit)

root.config(menu=mainmenu)
#

