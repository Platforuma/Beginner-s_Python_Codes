'''
Label Widget
width
multiple line
'''
from tkinter import *

root = Tk()
root.title('Demo')

root.configure(bg='lightblue')
##label_1 = Label(root)
##label_1 = Label(root, text='Hello World!')
##label_1 = Label(root, text='Hello World!', bg='#b20000', fg='white')
label_1 = Label(root,
                text='text in single line',
                bg='#b20000',
                fg='white',
                font='Times 32 bold italic',
                width = 20)
label_1.pack()

label_2 = Label(root,
                text='Text in \n in two lines',
                bg='#00b200',
                fg='white',
                font='Verdanta 16 italic',
                width = 10)
label_2.pack()

label_3 = Label(root,
                text='Text in \n\n in three lines',
                bg='#0000b2',
                fg='white',
                font='Ariel 64 bold',
                width = 30,
                height=20)
label_3.pack()

root.mainloop()
