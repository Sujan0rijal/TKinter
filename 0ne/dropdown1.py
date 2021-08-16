from tkinter import *

root = Tk()
root.title("Slider")
root.iconbitmap("D:/hello.ico")

def show():
    mylabel = Label(root, text=clicked.get()).pack()

clicked = StringVar()
clicked.set("sujan")

drop = OptionMenu(root, clicked, "sujan", "ram" , "shyam" , "hari", "krishna")
drop.pack()

mybutton = Button(root, text="show selection", command=show).pack()
mainloop()