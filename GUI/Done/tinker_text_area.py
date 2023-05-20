#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

# text widget
# functions like a text area, you can enter multiple lines of text

from tkinter import *

submit_button = lambda : print(my_text_area.get('1.0',END))

my_window = Tk() # instantiate an instance of a window
my_window.geometry('420x420')
my_window.title("window title")
my_window.config(background='black')
my_window.iconphoto(True,PhotoImage(file='image.png'))


my_submit_button = Button(my_window,
    text='Submit',
    command=submit_button
)

my_text_area = Text(my_window,
    fg='white',
    bg='black',
    font=('Ink Free',12),
    height=3,
    padx=5,
    pady=5,
)

my_submit_button.pack()
my_text_area.pack()

my_window.mainloop() # will place window on computer screen and will listen to events