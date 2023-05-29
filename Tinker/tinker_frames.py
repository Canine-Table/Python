#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

# frame
# a rectangular container to group and hold widgets

from tkinter import *

my_window = Tk() # instantiate an instance of a window
my_window.geometry('420x420')
my_window.title("window title")
my_window.config(background='black')
my_window.iconphoto(True,PhotoImage(file='image.png'))

my_frame = Frame(my_window,relief=SUNKEN,bg='gray')
w_button = Button(my_frame, text='W',font=('Consolas',23),width=3).pack(side=TOP)
a_button = Button(my_frame, text='A',font=('Consolas',23),width=3).pack(side=LEFT)
s_button = Button(my_frame, text='S',font=('Consolas',23),width=3).pack(side=LEFT)
d_button = Button(my_frame, text='D',font=('Consolas',23),width=3).pack(side=LEFT)
my_frame.place(x=0,y=0)

my_window.mainloop() # will place window on computer screen and will listen to events