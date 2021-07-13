from tkinter import *


run = Tk()
run.geometry("400x250")

name = Label(run, text ='Name').place(x = 30,y = 50)
address = Label(run, text = "Address").place(x = 30, y = 90)
contact = Label(run, text = "Contact").place(x= 30, y= 130)
e1 = Entry(run).place(x = 80, y = 50)
e2 =Entry(run).place(x = 80, y = 90)
e3 =Entry(run).place(x= 95, y = 130)

run.mainloop()