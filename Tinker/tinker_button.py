#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

from tkinter import *

num = 0
def clicked():
    global num
    num += 1
    print('clicked:',num)

my_window = Tk() # instantiate an instance of a window
my_window.geometry('920x920')
my_window.title("window title")
my_window.config(background='black')
my_image = PhotoImage(file='image.png')
my_window.iconphoto(True,my_image)

my_button = Button(my_window,
    text='Click Me',
    command=clicked,
    fg='white',
    bg='indigo',
    font=('Comic Sans',30,'italic'),
    activebackground='brown',
    activeforeground='yellow',
    state=ACTIVE,
    image=my_image,
    compound='bottom',
)

my_button.pack()

my_window.mainloop() # will place window on computer screen and will listen to events
