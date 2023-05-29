#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

from tkinter import *


def display_checked():
    match checked.get():
        case 1:
            print('agree :)')
        case 0:
            print('deny :(')

my_window = Tk() # instantiate an instance of a window

my_window.geometry('420x100')
my_window.title("window title")
my_window.config(background='black')
my_window.iconphoto(True,PhotoImage(file='image.png'))
checked = IntVar()

check_button = Checkbutton(my_window,
    text='a checkbutton',
    variable=checked,
    offvalue=0,
    onvalue=1,
    command=display_checked,
    activebackground='green',
    activeforeground='white',
    fg='white',
    padx=10,
    pady=5,
    bg='green',
    image=(my_photo := PhotoImage(file='icon_one.png')),
    compound=LEFT
)
check_button.pack()

my_window.mainloop() # will place window on computer screen and will listen to events