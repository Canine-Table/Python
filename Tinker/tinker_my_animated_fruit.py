#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

from tkinter import *
from time import *

def move_up_down(value):
    my_canvas.move(my_canvas_image,0,value)

def move_left_right(value):
    my_canvas.move(my_canvas_image,value,0)

my_window = Tk() # instantiate an instance of a window
my_window.geometry('420x420')
my_window.title("bouncy fruit")
my_window.config(background='black')
my_window.iconphoto(True,PhotoImage(file='image.png'))

my_canvas = Canvas(my_window)
my_photo = PhotoImage(file='icon_three.png')

my_canvas_image = my_canvas.create_image(0,0,image=my_photo,anchor=NW)
my_canvas.pack(expand=True,fill=BOTH,padx=1,pady=1)

def main():
    x = 10
    y = 10
    while True:
        try:
            sleep(0.01)
            wx = int(my_window.winfo_geometry().split('x')[0])
            wy = int(str(my_window.winfo_geometry().split('x')[1]).split('+')[0])
            cx = round(my_canvas.coords(my_canvas_image)[0])
            cy = round(my_canvas.coords(my_canvas_image)[1])
            tx=wx-cx
            ty=wy-cy
            if tx <= 64:
                x = -10
            elif tx >= wx:
                x = 10
            if ty <= 64:
                y = -10
            elif ty >= wy:
                y = 10
            move_up_down(y)
            move_left_right(x)
            my_window.update()
        except TclError:
            exit()
if __name__ == '__main__':
    main()

my_window.mainloop() # will place window on computer screen and will listen to events