#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

# grid()
# gep,etry manager that organizes widgets in a table-like structure in a parent

from tkinter import *

my_window = Tk() # instantiate an instance of a window
my_window.geometry('840x420')
my_window.title("window title")
my_window.config(background='black')
my_window.iconphoto(True,PhotoImage(file='image.png'))

Label(my_window,text='First Name: ',width=15).grid(row=0,column=0)
Entry(my_window,width=15).grid(row=0,column=1)
Label(my_window,text='Last Name: ',width=15).grid(row=1,column=0)
Entry(my_window,width=15).grid(row=1,column=1)
Label(my_window,text='Phone Number: ',width=15).grid(row=2,column=0)
Entry(my_window,width=15).grid(row=2,column=1)
Label(my_window,text='Email Address: ',width=15).grid(row=3,column=0)
Entry(my_window,width=15).grid(row=3,column=1)
Button(my_window,text='Submit Query',width=15).grid(row=4,column=1,columnspan=1)
my_window.mainloop() # will place window on computer screen and will listen to events