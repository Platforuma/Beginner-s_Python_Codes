'''
Grid 
'''
from tkinter import *

w = 5
h = 2
font_style = 'Times 32 bold'

root = Tk()

label_1 = Label(root,
                text='(0,0)',
                width=w,
                height=h,
                borderwidth=6,
                relief='solid',
                font=font_style)
label_1.grid(row=0, column=0)

label_2 = Label(root, text='(1,0)',
                width=w,
                height=h,
                borderwidth=6,
                relief='solid',
                font=font_style)
label_2.grid(row=1, column=0)

label_3 = Label(root, text='(2,0)',
                width=w,
                height=h,
                borderwidth=6,
                relief='solid',
                font=font_style)
label_3.grid(row=2, column=0)

label_4 = Label(root, text='(0,1)',
                width=w,
                height=h,
                borderwidth=6,
                relief='solid',
                font=font_style)
label_4.grid(row=0, column=1)

label_5 = Label(root, text='(1,1)',
                width=w,
                height=h,
                borderwidth=6,
                relief='solid',
                font=font_style)
label_5.grid(row=1, column=1)

label_6 = Label(root, text='(2,1)',
                width=w,
                height=h,
                borderwidth=6,
                relief='solid',
                font=font_style)
label_6.grid(row=2, column=1)

label_7 = Label(root, text='(0,2)',
                width=w,
                height=h,
                borderwidth=6,
                relief='solid',
                font=font_style)
label_7.grid(row=0, column=2)

label_8 = Label(root, text='(1,2)',
                width=w,
                height=h,
                borderwidth=6,
                relief='solid',
                font=font_style)
label_8.grid(row=1, column=2)

label_9 = Label(root, text='(2,2)',
                width=w,
                height=h,
                borderwidth=6,
                relief='solid',
                font=font_style)
label_9.grid(row=2, column=2)





root.mainloop()
