from tkinter import *
root = Tk()

myLabel1 = Label(root, text = 'Tkinter Program Beginning')
myLabel2 = Label(root, text = "I am Sujan Rijal")
myLabel3 = Label(root, text = 'Hello World!!')

myLabel1.grid(row = 0 , column = 0)
myLabel2.grid(row = 1 , column = 2)
myLabel3.grid(row = 1, column  = 0)

root.mainloop()