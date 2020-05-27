'''
Radio Buttons
'''
from tkinter import *

root = Tk()
root.title('Registration Form')
root.geometry('300x200')

frame_1 = Frame(root)
heading_label = Label(frame_1, text='Registration Form',
                      font='Times 16 bold', pady=10)
first_name_label = Label(frame_1, text='First Name: ', width=15, anchor=E)
last_name_label = Label(frame_1, text='Last Name: ', width=15, anchor=E)
gender_label = Label(frame_1, text='Gender: ', width=15, anchor=E)
mobile_number_label = Label(frame_1, text='Contact Number: ', width=15, anchor=E)
email_label = Label(frame_1, text='Email: ', width=15, anchor=E)
city_label = Label(frame_1, text='City: ', width=15, anchor=E)

first_name_entry = Entry(frame_1)
last_name_entry = Entry(frame_1)
gender_entry = Entry(frame_1)
mobile_number_entry = Entry(frame_1)
email_entry = Entry(frame_1)
city_entry = Entry(frame_1)

frame_1.pack()
heading_label.grid(row=0,columnspan=2)
first_name_label.grid(row=1,column=0)
last_name_label.grid(row=2,column=0)
gender_label.grid(row=3,column=0)
mobile_number_label.grid(row=4,column=0)
email_label.grid(row=5,column=0)
city_label.grid(row=6,column=0)

first_name_entry.grid(row=1,column=1)
last_name_entry.grid(row=2,column=1)
gender_entry.grid(row=3,column=1)
mobile_number_entry.grid(row=4,column=1)
email_entry.grid(row=5,column=1)
city_entry.grid(row=6,column=1)

root.mainloop()
