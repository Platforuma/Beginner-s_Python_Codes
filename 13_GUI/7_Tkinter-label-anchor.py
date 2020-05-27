'''
Label Widget
Anchor
'''
from tkinter import *

w=10
h=2

root = Tk()

root.title('Demo')
root.configure(bg='lightblue')

label_1 = Label(root,
                text='Highlight',
                font='Times 10 italic')
label_1.pack()

label_2 = Label(root,
                text='CENTER',
                font='Times 40 italic',
                borderwidth=5,
                width=w,
                height=h,
                relief='solid',
                anchor=CENTER)
label_2.pack()

label_3 = Label(root,
                text='NORTH',
                font='Times 40 italic',
                borderwidth=5,
                width=w,
                height=h,
                relief='solid',
                anchor=N)
label_3.pack()

label_4 = Label(root,
                text='SOUTH',
                font='Times 40 italic',
                borderwidth=5,
                width=w,
                height=h,
                relief='solid',
                anchor=S)
label_4.pack()

label_5 = Label(root,
                text='EAST',
                font='Times 40 italic',
                borderwidth=5,
                width=w,
                height=h,
                relief='solid',
                anchor=E)
label_5.pack()

label_6 = Label(root,
                text='WEST',
                font='Times 40 italic',
                borderwidth=5,
                width=w,
                height=h,
                relief='solid',
                anchor=W)
label_6.pack()



root.mainloop()
