import tkinter as tk
ak=tk.Tk()
ak.geometry("100x200")
OptionList=[
    "1",
    "2",
    "3",
    "4",
    "5",
    "6"
]
v=tk.StringVar(ak)
v.set(OptionList[0])

opt=tk.OptionMenu(ak,v,*OptionList)
opt.config(width=90, font=("Helvetica",12))
opt.pack()
ak.mainloop()
