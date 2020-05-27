'''
Label Widget
Border
'''
from tkinter import *

root = Tk()

root.title('Demo')
root.configure(bg='lightblue')

label_1 = Label(root,
                text='Border',
                font='Times 40 italic',
                borderwidth=10,
                anchor=CENTER)
label_1.pack()

label_2 = Label(root,
                text='Solid',
                font='Times 40 italic',
                borderwidth=10,
                relief='solid',
                anchor=CENTER)
label_2.pack()

label_3 = Label(root,
                text='Raised',
                font='Times 40 italic',
                borderwidth=20,
                relief='raised')
label_3.pack()

label_4 = Label(root,
                text='Sunken',
                font='Times 40 italic',
                borderwidth=20,
                relief='sunken',
                anchor=CENTER)
label_4.pack()

label_5 = Label(root,
                text='Ridge',
                font='Times 40 italic',
                borderwidth=20,
                relief='ridge',
                anchor=CENTER)
label_5.pack()

label_6 = Label(root,
                text='Groove',
                font='Times 40 italic',
                borderwidth=20,
                relief='groove')
label_6.pack()

label_7 = Label(root,
                text='Flat',
                font='Times 40 italic',
                borderwidth=20,
                relief='flat')
label_7.pack()

root.mainloop()
