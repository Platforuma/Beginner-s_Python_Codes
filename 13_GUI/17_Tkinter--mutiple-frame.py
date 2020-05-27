'''
Multiple Frame
'''
from tkinter import *

root = Tk()

frame_1 = Frame(root, bg='red', width=300, height=300)
frame_1.grid(row=0, column=0)

frame_2 = Frame(root, bg='blue', width=300, height=300)
frame_2.grid(row=1, column=1)

root.mainloop()
