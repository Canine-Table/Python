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

my_window.bind('<Button-1>',lambda event: print('Left Click\n','\nX:',event.x,'\nY:',event.y,'\n'))
my_window.bind('<Button-2>',lambda event: print('Middle Click\n','\nX:',event.x,'\nY:',event.y,'\n'))
my_window.bind('<Button-3>',lambda event: print('Right Click\n','\nX:',event.x,'\nY:',event.y,'\n'))
my_window.bind('<Enter>',lambda event: print('Entered the Window\n','\nX:',event.x,'\nY:',event.y,'\n'))
my_window.bind('<Leave>',lambda event: print('Exited the Window\n','\nX:',event.x,'\nY:',event.y,'\n'))
my_window.bind('<Motion>',lambda event: print('Mouse is moving within the Window\n','\nX:',event.x,'\nY:',event.y,'\n'))


my_window.mainloop() # will place window on computer screen and will listen to events
