from tkinter import *

root = Tk()
root.title("Slider")
root.iconbitmap("D:/hello.ico")

def show():
    mylabel= Label(root, text=clicked.get()).pack()

options= [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "friday",
    "saturday"
]

clicked = StringVar()
clicked.set("sunday")

drop = OptionMenu(root, clicked,*options)
drop.pack()

mybutton = Button(root, text="show selections",command = show).pack()

mainloop()