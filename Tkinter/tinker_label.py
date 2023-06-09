#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

from tkinter import *


my_window = Tk() # instantiate an instance of a window
my_window.geometry('680x420')
my_window.title("window title")
my_window.config(background='black')

my_image = PhotoImage(file='image.png')
my_window.iconphoto(True,my_image)

my_label = Label(my_window,
    text="Hello World",
    font=('Arial',40,'bold'),
    fg='white',
    bg='gray',
    relief=RAISED,
    borderwidth=10,
    pady=20,
    image=my_image,
    padx=10,
    compound='bottom',
)


my_label.pack() # my_label.place(x=0,y=0)

my_window.mainloop() # will place window on computer screen and will listen to events
