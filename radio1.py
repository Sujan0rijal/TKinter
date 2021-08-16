from tkinter import *

root = Tk()
root.title("Radio Button")

MODES = [
    ("ram","ram"),
    ("shyam","shyam"),
    ("sunil","sunil"),
    ("hari","hari")
]

random = StringVar()
random.set("ram")

for text, mode in MODES:
    Radiobutton(root, text = text , variable = random , value = mode).pack(anchor = W)


def clicked(value):
    mylabel = Label(root, text= value)
    mylabel.pack()

myButton = Button(root, text= "click", command = lambda :clicked(random.get())).pack()


root.mainloop()
