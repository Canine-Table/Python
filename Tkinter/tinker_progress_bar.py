#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images


from tkinter import *
from tkinter.ttk import *
import time

def downloading_file():
    increment = 10
    while my_progress['value'] <= 100:
        time.sleep(1)
        my_progress['value']+=increment
        if my_progress['value'] >= 100:
            percent.set(str('task completed'))
        else:
            percent.set(str(round(my_progress['value']))+'%')
        my_window.update_idletasks()
    time.sleep(1)
    my_window.destroy()

my_window = Tk() # instantiate an instance of a window
my_window.geometry('420x420')
my_window.title("window title")
my_window.config(background='gray')
my_window.iconphoto(True,PhotoImage(file='image.png'))

my_progress = Progressbar(my_window,orient=HORIZONTAL,length=300)
my_progress.pack(padx=10,pady=10)
Button(my_window,text='Click to Download',command=downloading_file).pack(padx=10,pady=10)
percent = StringVar()
percent.set('0%')

Label(my_window,textvariable=percent).pack(padx=10,pady=10)

my_window.mainloop() # will place window on computer screen and will listen to events
