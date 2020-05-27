'''
Label color project
'''
from tkinter import *

root = Tk()

def red_color_placer():
    label_2['bg'] = 'red'
    label_1['text'] = 'The color of the label is: red'
    label_1['fg'] = 'red'
    
def green_color_placer():
    label_2['bg'] = 'green'
    label_1['text'] = 'The color of the label is: green'
    label_1['fg'] = 'green'
    
def blue_color_placer():
    label_2['bg'] = 'blue'
    label_1['text'] = 'The color of the label is: blue'
    label_1['fg'] = 'blue'
    
label_1 = Label(root,
                text='The color of the label is: white',
                font='Times 16 italic',
                width=30,
                height=2)
label_1.grid(row=2, columnspan=3)

label_2= Label(root, width=20, height=9, bg='white', bd=8, relief='solid')
label_2.grid(row=0, columnspan=3)

red_button = Button(root, text='RED', width=6, command=red_color_placer)
red_button.grid(row=1,column=0)

green_button = Button(root, text='GREEN', width=6, command=green_color_placer)
green_button.grid(row=1,column=1)

blue_button = Button(root, text='BLUE', width=6, command=blue_color_placer)
blue_button.grid(row=1,column=2)



root.mainloop()
