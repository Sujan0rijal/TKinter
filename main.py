from tkinter import *

root = Tk()

redbutton = Button(root, text = 'LEFT', fg = 'green')
redbutton.pack( side = LEFT)

greenbutton = Button(root, text = 'RIGHT' , fg = 'black')
greenbutton.pack(side = RIGHT)

bluebottton = Button(root, text = 'TOP', fg = 'blue')
bluebottton.pack(side = TOP)

blackbotton = Button(root, text ='BOTTOM' , fg = 'red')
blackbotton.pack(side = BOTTOM)

root.mainloop()