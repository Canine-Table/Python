#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

from tkinter import *

def move_up(event):
    my_canvas.move(my_canvas_image,0,-10)

def move_left(event):
    my_canvas.move(my_canvas_image,-10,0)

def move_down(event):
    my_canvas.move(my_canvas_image,0,10)

def move_right(event):
    my_canvas.move(my_canvas_image,10,0)

my_window = Tk() # instantiate an instance of a window
my_window.geometry('820x820')
my_window.title("window title")
my_window.config(background='black')
my_window.iconphoto(True,PhotoImage(file='image.png'))

my_canvas = Canvas(my_window)
my_photo = PhotoImage(file='icon_three.png')

my_canvas_image = my_canvas.create_image(0,0,image=my_photo,anchor=NW)

my_canvas.pack(expand=True,fill=BOTH,padx=1,pady=1)

my_window.bind('<w>',move_up)
my_window.bind('<W>',move_up)
my_window.bind('<Up>',move_up)

my_window.bind('<a>',move_left)
my_window.bind('<A>',move_left)
my_window.bind('<Left>',move_left)

my_window.bind('<s>',move_down)
my_window.bind('<S>',move_down)
my_window.bind('<Down>',move_down)

my_window.bind('<d>',move_right)
my_window.bind('<D>',move_right)
my_window.bind('<Right>',move_right)

my_window.mainloop() # will place window on computer screen and will listen to events