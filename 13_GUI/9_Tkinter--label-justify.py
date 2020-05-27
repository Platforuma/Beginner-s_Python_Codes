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
                text='Justify Right\nJustify Left\nJustify Center',
                font='Times 20 italic',
                borderwidth=5,
                width=w,
                height=h,
                relief='solid',
                justify=LEFT
                )
label_2.pack()

label_3 = Label(root,
                text='Justify Right\nJustify Left\nJustify Center',
                font='Times 20 italic',
                borderwidth=5,
                width=w,
                height=h,
                relief='solid',
                justify=RIGHT
                )
label_3.pack()

label_4 = Label(root,
                text='Justify Right\nJustify Left\nJustify Center',
                font='Times 20 italic',
                borderwidth=5,
                width=w,
                height=h,
                relief='solid',
                justify=CENTER
                )
label_4.pack()


root.mainloop()
