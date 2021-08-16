from tkinter import *


root = Tk()
root.title('Database GUI')
root.iconbitmap("D:/hello.ico")
root.geometry("300x480")

class One:

    def __init__(self,master):
        myFrame = Frame(master)
        myFrame.pack()

        self.myButton = Button(root, text="Click Me",command=self.click)
        self.myButton.pack(pady=20)

    def click(self):
        print("Button Clicked")

e = One(root)
root.mainloop()