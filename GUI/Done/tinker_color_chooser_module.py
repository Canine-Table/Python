#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

from tkinter import *
from random import choice
from tkinter import colorchooser # this is a submodule so its not included with (from tkinter import *)

def select_color():

    for i in colorchooser.askcolor():
        match my_value := i[0]:
            case '#':
                my_window.config(bg=i)
                print('your selected the {} value of:'.format('HEX'),i)
            case _:
                print('your selected the {} value of:'.format('RGB'),i)

def generate_random():
    def generate():
        my_hex = '#'
        for i in range(0,6):
            my_hex += str(choice([i for i in range(0,10)]+['A','B','C','D','E','F']))
        return my_hex
    my_window.config(bg=generate())
    my_label.config(fg=generate(),bg=generate())
    my_button.config(fg=generate(),bg=generate(),activebackground=generate(),activeforeground=generate())
    my_generate_random_button.config(fg=generate(),bg=generate(),activebackground=generate(),activeforeground=generate())


my_window = Tk() # instantiate an instance of a window
my_window.geometry('820x820')
my_window.title("window title")
my_window.config(background='black')
my_window.iconphoto(True,PhotoImage(file='image.png'))

my_button = Button(my_window,
    text='change color?',
    command=select_color,
)

my_generate_random_button = Button(my_window,
    text='randomly change color?',
    command=generate_random,
)
my_label = Label(my_window,
    text='My Label',
    font=('Constantia',24),
    fg='white',
    bg='black'
)

my_button.pack()
my_generate_random_button.pack()
my_label.pack()
my_window.mainloop() # will place window on computer screen and will listen to events
