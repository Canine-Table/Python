#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

from tkinter import *

def create_window():

    def destroy():
        try:
            my_window.destroy()
        except TclError:
            pass
    new_window = Toplevel()

    # Toplevel() windows 'on top' of other windows. linked
    # Tk() is a new windows independent from other windows.
    #  while Toplevel Windows are children of Tk() windows. all children will be killed
    # once the parent Tk() is exited.
    
    new_tk_window = Tk()
    my_destroy_button = Button(new_tk_window,text='DESTROY',command=destroy).pack(side=TOP)
    new_tk_window.mainloop()

my_window = Tk() # instantiate an instance of a window
my_window.geometry('420x420')
my_window.title("window title")
my_window.config(background='black')
my_window.iconphoto(True,PhotoImage(file='image.png'))

my_button = Button(my_window,
    text='New Window',
    command=create_window,
).place(x=0,y=0)

my_window.mainloop() # will place window on computer screen and will listen to events
