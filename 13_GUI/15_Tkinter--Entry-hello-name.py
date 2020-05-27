'''
Entry Widget
'''
from tkinter import *

def name_get():
    name = entry_1.get()
    city = entry_2.get()
    string_to_display = 'Hello' + name + city
    label_2 = Label(root, text=string_to_display, justify=RIGHT,
                font='Times 12 bold')
    label_2.grid(row=2,column=1)

root = Tk()

label_1 = Label(root, text='Enter the name: ',
                justify=RIGHT,
                font='Times 12 bold')
label_1.grid(row=0,column=0)

entry_1 = Entry(root)
entry_1.grid(row=0,column=1)

label_2 = Label(root, text='Enter the City: ',
                justify=RIGHT,
                font='Times 12 bold')
label_2.grid(row=1,column=0)

entry_2 = Entry(root)
entry_2.grid(row=1,column=1)


button_1 = Button(root, text='Click Me',font='Times 12 bold', command=name_get)
button_1.grid(row=2,column=0)

root.mainloop()
