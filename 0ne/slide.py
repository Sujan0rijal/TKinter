from tkinter import *

root = Tk()
root.title("Slider")
root.iconbitmap("D:/hello.ico")

vertical = Scale(root, from_=0 , to=450)
vertical.pack()

horizontal = Scale(root, from_=0, to=450, orient = HORIZONTAL)
horizontal.pack()

my_label= Label(root, text = horizontal.get()).pack()

def slide():
    my_label = Label(root, text = horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

my_button = Button(root, text= "Click Me", command = slide).pack()

mainloop()