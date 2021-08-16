from tkinter import *

root = Tk()
root.title("Slider")
root.iconbitmap("D:/hello.ico")

def show():
    mylabel=Label(root, text=var.get()).pack()

var = StringVar()
checkButton = Checkbutton(root, text= "check this button", variable= var, onvalue="On",
                          offvalue= "Off")
checkButton.deselect()
checkButton.pack()
my_button = Button(root, text = "Show Selection", command=show).pack()

mainloop()