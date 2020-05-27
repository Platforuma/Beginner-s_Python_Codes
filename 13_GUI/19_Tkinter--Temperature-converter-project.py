'''
Temperature converter
'''
from tkinter import *

root = Tk()

def fah_to_cel():
    fah = entry_1.get()
    cel = ((float(fah) - 32)*5)/9
    label_5 = Label(frame_1, text=str(cel))
    label_5.grid(row=2,column=1)
    
def cel_to_fah():
    cel = entry_2.get()
    fah = (float(cel) * (9/5)) + 32
    label_6 = Label(frame_2, text=str(fah))
    label_6.grid(row=2,column=1)

#frame 1
frame_1 = Frame(root, bd=4, relief='solid')
frame_1.grid(row=0,column=0)

#Frame 1 heading
label_1 = Label(frame_1, text='Fahrenheit to Celsius Converter',
                font = 'Times 14 bold')
label_1.grid(row=0,columnspan=2)

#label 1 Fahrenheit
label_3 = Label(frame_1, text='Fahrenheit: ',
                font = 'Times 12 bold')
label_3.grid(row=1,column=0)

#entry 1
entry_1 = Entry(frame_1)
entry_1.grid(row=1,column=1)

#Button 1
button_1 = Button(frame_1, text='Convert', command=fah_to_cel)
button_1.grid(row=2,column=0)

##################################################################
#frame 2
frame_2 = Frame(root, bd=4, relief='solid')
frame_2.grid(row=0,column=1)

#Frame 2 heading
label_2 = Label(frame_2, text='Celsius to Fahrenheit Converter',
                font = 'Times 14 bold')
label_2.grid(row=0,columnspan=2)

#label 2 Celcius
label_4 = Label(frame_2, text='Celsius: ',
                font = 'Times 12 bold')
label_4.grid(row=1,column=0)

#entry 2
entry_2 = Entry(frame_2)
entry_2.grid(row=1,column=1)

#Button 2
button_2 = Button(frame_2, text='Convert', command=cel_to_fah)
button_2.grid(row=2,column=0)

root.mainloop()
