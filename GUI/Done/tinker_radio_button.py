#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

# radio button
# similar to checkbox, but only one can be selected from a group

from tkinter import *

def get_selected():
    match selected.get():
        case 0:
            print('you selected one')
        case 1:
            print('you selected two')
        case 2:
            print('you selected three')
        case 3:
            print('you selected four')

my_window = Tk() # instantiate an instance of a window
my_window.geometry('420x420')
my_window.title("window title")
my_window.config(background='black')
my_image = PhotoImage(file='image.png')
my_window.iconphoto(True,my_image)

selected = IntVar()
radio_buttons = ['One','Two','Three','Four']
num = 0
for i in radio_buttons:
    my_radio_button = Radiobutton(my_window,
        value=num,
        text=i,
        variable=selected,
        padx=20,
        font=('impact',24),
        pady=10,
        indicatoron=0,
        width=360,
        command=get_selected,
    )
    num += 1
    my_radio_button.pack(anchor=W)

my_window.mainloop() # will place window on computer screen and will listen to events
