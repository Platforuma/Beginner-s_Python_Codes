'''
Entry Widget
'''

from tkinter import *

root = Tk()

name_label = Label(root, text="First Name: ", width = 10, anchor=E)
name_label.grid(row=0,column=0)

last_label = Label(root, text="Last Name: ", width = 10, anchor=E)
last_label.grid(row=1,column=0)

city_label = Label(root, text="City: ", width = 10, anchor=E)
city_label.grid(row=2,column=0)

name_entry = Entry(root)
name_entry.grid(row=0,column=1)

last_entry = Entry(root)
last_entry.grid(row=1,column=1)

city_entry = Entry(root)
city_entry.grid(row=2,column=1)

root.mainloop()
