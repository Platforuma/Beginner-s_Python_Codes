'''
Radio button 
'''
from tkinter import *

def get_options():
    ques_1 = a_var.get()
    ques_2 = b_var.get()
    ques_3 = c_var.get()
    ques_4 = d_var.get()
    print('The choice for quest_1: ', str(ques_1))
    print('The choice for quest_2: ', str(ques_2))
    print('The choice for quest_3: ', str(ques_3))
    print('The choice for quest_4: ', str(ques_4))
    submission_label = Label(root, text='Thank you for the submission!', font='Verdanta 14 bold italic',
                             bd=4, relief='ridge', pady=4, padx=20).grid(row=10,columnspan=4)

root = Tk()

a_var = IntVar()
b_var = IntVar()
c_var = IntVar()
d_var = IntVar()

heading_label = Label(root, text='Quiz', width=6, font='Times 16 bold', bd=4, relief='groove', pady=4).grid(row=0,columnspan=4)

a_label = Label(root, text='1. Capial of India?', width=45, font='Times 12', anchor=W).grid(row=1,columnspan=4)
a1_rbutton = Radiobutton(root, text='Delhi', variable=a_var, value=0).grid(row=2,column=0)
a2_rbutton = Radiobutton(root, text='Mumbai', variable=a_var, value=1).grid(row=2,column=1)
a3_rbutton = Radiobutton(root, text='Bangalore', variable=a_var, value=2).grid(row=2,column=2)
a4_rbutton = Radiobutton(root, text='Indore', variable=a_var, value=3).grid(row=2,column=3)

b_label = Label(root, text='2. Total states in India?', width=45, font='Times 12', anchor=W).grid(row=3,columnspan=4)
b1_rbutton = Radiobutton(root, text='28', variable=b_var, value=0).grid(row=4,column=0)
b2_rbutton = Radiobutton(root, text='29', variable=b_var, value=1).grid(row=4,column=1)
b3_rbutton = Radiobutton(root, text='7', variable=b_var, value=2).grid(row=4,column=2)
b4_rbutton = Radiobutton(root, text='30', variable=b_var, value=3).grid(row=4,column=3)

c_label = Label(root, text='3. Best Place to learn Python?', width=45, font='Times 12', anchor=W).grid(row=5,columnspan=4)
c1_rbutton = Radiobutton(root, text='Online site', variable=c_var, value=0).grid(row=6,column=0)
c2_rbutton = Radiobutton(root, text='Coaching classes', variable=c_var, value=1).grid(row=6,column=1)
c3_rbutton = Radiobutton(root, text='College', variable=c_var, value=2).grid(row=6,column=2)
c4_rbutton = Radiobutton(root, text='Platforuma', variable=c_var, value=3).grid(row=6,column=3)

d_label = Label(root, text='4. Best Instructor ever?', width=45, font='Times 12', anchor=W).grid(row=7,columnspan=4)
d1_rbutton = Radiobutton(root, text='College faculty', variable=d_var, value=0).grid(row=8,column=0)
d2_rbutton = Radiobutton(root, text='Saral sir', variable=d_var, value=1).grid(row=8,column=1)
d3_rbutton = Radiobutton(root, text='Joshi Sir', variable=d_var, value=2).grid(row=8,column=2)
d4_rbutton = Radiobutton(root, text='Sharma sir', variable=d_var, value=3).grid(row=8,column=3)

submit_button = Button(root, text='Submit', font='Times 12 bold', bg='lightgrey', width=8, pady=4, command=get_options).grid(row=9,columnspan=4)
 
root.mainloop()
