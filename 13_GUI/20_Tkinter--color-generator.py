'''
Random color generator
'''

from tkinter import *
from random import *

hexa_char = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

def random_color_generator():
    color_code = '#'
    for i in range(0,6):
        color_code += choice(hexa_char)
    color_hexa_code = 'The color code is: ', color_code
    label_2['text'] = color_hexa_code
    label_2['font'] = 'Verdanta 16 italic'
    label_2['fg'] = color_code
    label_1['bg']=color_code
    return color_code

##print(random_color_generator())

root = Tk()

label_1 = Label(root, width=30, height=10, bd=4, relief='sunken')
label_1.grid(row=0,columnspan=3)

button_1 = Button(root, text='Color Generator',
                  font='Times 14 bold',
                  command=random_color_generator)
button_1.grid(row=1,column=1)

label_2 = Label(root, bd=2, relief='raised', padx=40, pady=3)
label_2.grid(row=2,columnspan=3)

root.mainloop()
