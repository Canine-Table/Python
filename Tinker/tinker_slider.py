#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

from tkinter import *

def submited():
    print(my_scale.get())

my_window = Tk() # instantiate an instance of a window
my_window.geometry('420x420')
my_window.title("window title")
my_window.config(background='black')
my_window.iconphoto(True,PhotoImage(file='image.png'))
top_image = PhotoImage(file='icon_one.png')
bottom_image = PhotoImage(file='icon_two.png')
my_scale = Scale(my_window,
    from_=100,
    to=0,
    length=200,
    width=50,
    orient=VERTICAL,
    font=('Consolas',10),
    tickinterval=20,
    showvalue=1,
    troughcolor='#69EAFF',
    fg='#FF1C00',
    bg='#555555',
)

my_button = Button(my_window,
    text='submit',
    command=submited,
)

top_label = Label(image=top_image)
bottom_label = Label(image=bottom_image)
my_scale.set((my_scale['from']-my_scale['to'])/2+my_scale['to'])
top_label.pack()
my_scale.pack()
bottom_label.pack()
my_button.pack()
my_window.mainloop() # will place window on computer screen and will listen to events
