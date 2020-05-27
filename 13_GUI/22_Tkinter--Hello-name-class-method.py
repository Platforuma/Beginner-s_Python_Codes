'''
Hello World
OOPs Method
'''

from tkinter import *

class HelloNameFrame(Frame):

    def __init__(self, the_window):

        Frame.__init__(self, the_window)

        self.user_name = StringVar()
        self.display_string = StringVar()
                
        self.label_1 = Label(self, text='Name: ').grid(row=0,column=0)
        self.name = Entry(self, textvariable=self.user_name).grid(row=0,column=1)
        self.button = Button(self,text='Click Me', command=self.display_output).grid(row=1,column=0)
        self.display_label = Label(self, textvariable = self.display_string, relief='solid', width=15).grid(row=1,column=1)

    def display_output(self):
        self.display_string.set('Hello ' +  self.user_name.get())
        

root = Tk()
frame_A = HelloNameFrame(root)
frame_A.grid(row=0,column=0)
root.mainloop()
         
