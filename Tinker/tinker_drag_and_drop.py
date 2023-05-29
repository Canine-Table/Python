#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

from tkinter import *

def drag_start(event):
    my_widget = event.widget
    my_widget.startX = event.x
    my_widget.startY = event.y

def drag_motion(event):
    my_widget = event.widget
    new_x = my_widget.winfo_x() - my_widget.startX + event.x
    new_y = my_widget.winfo_y() - my_widget.startY + event.y
    my_widget.place(x=new_x,y=new_y)

my_window = Tk() # instantiate an instance of a window
my_window.geometry('420x420')
my_window.title("window title")
my_window.config(background='black')
my_window.iconphoto(True,PhotoImage(file='image.png'))

my_label_1 = Label(my_window,bg='green',width=10,height=5)
my_label_1.place(x=0,y=0)
my_label_1.bind('<Button-1>',drag_start)
my_label_1.bind('<B1-Motion>',drag_motion)

my_label_2 = Label(my_window,bg='blue',width=10,height=5)
my_label_2.place(x=200,y=0)
my_label_2.bind('<Button-1>',drag_start)
my_label_2.bind('<B1-Motion>',drag_motion)

my_label_3 = Label(my_window,bg='yellow',width=10,height=5)
my_label_3.place(x=0,y=200)
my_label_3.bind('<Button-1>',drag_start)
my_label_3.bind('<B1-Motion>',drag_motion)

my_label_4 = Label(my_window,bg='red',width=10,height=5)
my_label_4.place(x=200,y=200)
my_label_4.bind('<Button-1>',drag_start)
my_label_4.bind('<B1-Motion>',drag_motion)

my_window.mainloop() # will place window on computer screen and will listen to events