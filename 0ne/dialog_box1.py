from tkinter import *
from PIL inport ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Dialog Box')
root.iconbitmap("D:/hello.ico")

def open():
    global my name
    root.filename = filedialog.askopenfile(initialdir = "/Downloads",
                                           title = "Select a file",
                                           filrtypes= (("png files", "*.png"),
                                                       ("all files", "*.*")))
    my_image = ImageTk.Photoimage(Image.opem(root.filename))
    my_image_label= Label(image= my_image).pack()


my_button = Button(root, text= "Open File", command = open).pack()

mainloop()