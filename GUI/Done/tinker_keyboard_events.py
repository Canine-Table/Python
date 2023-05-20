#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

from tkinter import *

my_window = Tk() # instantiate an instance of a window
my_window.geometry('420x420')
my_window.title("window title")
my_window.config(background='black')
my_window.iconphoto(True,PhotoImage(file='image.png'))

my_window.bind('<Key>',lambda event: my_label.config(text=event.keysym))

my_window.bind('<Return>',lambda event: print('you pressed enter!!'))
my_label = Label(my_window,font=('Helvetica',100))
my_label.config(text='press a key')
my_label.pack(padx=10,pady=10)

my_label.pack()
my_window.mainloop() # will place window on computer screen and will listen to events
