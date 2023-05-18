#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

from tkinter import *


def display_checked():
    if checked.get() == 1:
        print('agree :)')
    elif checked.get() == 0:
        print('deny :(')

my_window = Tk() # instantiate an instance of a window

my_window.geometry('820x820')
my_window.title("window title")
my_window.config(background='black')
my_image = PhotoImage(file='image.png')
my_window.iconphoto(True,my_image)
checked = IntVar()

check_button = Checkbutton(my_window,
    text='a checkbutton',
    variable=checked,
    offvalue=0,
    onvalue=1,
    command=display_checked,
    activebackground='black',
    activeforeground='white',
    fg='white',
    bg='black',
    image=my_image,
    compound=BOTTOM
)
check_button.pack()

my_window.mainloop() # will place window on computer screen and will listen to events