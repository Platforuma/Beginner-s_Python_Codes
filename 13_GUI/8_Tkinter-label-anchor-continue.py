'''
Label Widget
Anchor continue
'''
from tkinter import *

w=50
h=5

root = Tk()

root.title('Demo')
root.configure(bg='lightblue')

label_1 = Label(root,
                text='Highlight',
                font='Times 10 italic')
label_1.pack()

label_2 = Label(root,
                text='NORTH EAST',
                font='Times 20 italic',
                borderwidth=5,
                width=w,
                height=h,
                relief='solid',
                anchor=NE)
label_2.pack()

label_3 = Label(root,
                text='SOUTH EAST',
                font='Times 20 italic',
                borderwidth=5,
                width=w,
                height=h,
                relief='solid',
                anchor=SE)
label_3.pack()

label_4 = Label(root,
                text='SOUTH WEST',
                font='Times 20 italic',
                borderwidth=5,
                width=w,
                height=h,
                relief='solid',
                anchor=SW)
label_4.pack()

label_5 = Label(root,
                text='NORTH WEST',
                font='Times 20 italic',
                borderwidth=5,
                width=w,
                height=h,
                relief='solid',
                anchor=NW)
label_5.pack()

root.mainloop()
