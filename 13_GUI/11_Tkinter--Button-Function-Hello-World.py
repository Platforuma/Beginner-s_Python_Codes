'''
Button Widget
'''
from tkinter import *

def hello_world():
    label_2 = Label(root, text='Hello World!')
    label_2.pack()

root = Tk()

label_1 = Label(root, text='Click Me to print Hello')
label_1.pack()

button_1 = Button(root, text='Click', command=hello_world)
button_1.pack()

root.mainloop()
