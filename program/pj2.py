from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.title("Akash")
root.geometry("250x400")
root.minsize(250,360)
#root.maxsize(250,360)
image=Image.open("av.jpeg")
photo=ImageTk.PhotoImage(image)
label=Label(image=photo)
label.configure(bg="black",height=360)
label.pack()
Akash = Label(root,text="Avinash Singh").place(x=140,y=140)
root.mainloop()