'''
Button Widget
'''
from tkinter import *

root = Tk()

label_1 = Label(root, text='Click Me to print Hello')
label_1.pack()

button_1 = Button(root, text='Click')
button_1.pack()

root.mainloop()
