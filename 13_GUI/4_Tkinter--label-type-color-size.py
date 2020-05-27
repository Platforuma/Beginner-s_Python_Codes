'''
Label Widget
'''
from tkinter import *

root = Tk()
root.title('Demo')

root.configure(bg='lightblue')
##label_1 = Label(root)
##label_1 = Label(root, text='Hello World!')
##label_1 = Label(root, text='Hello World!', bg='#b20000', fg='white')
label_1 = Label(root,
                text='Hello World!',
                bg='#b20000',
                fg='white',
                font='Times 32 bold italic')
label_1.pack()

root.mainloop()
