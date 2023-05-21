#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

from tkinter import *
from time import *

def update_clock():
    time_string = strftime("%A\n%I:%M:%S %p\n%B %d, %Y")
    my_clock_label.config(text=time_string)
    my_clock_label.after(1000,update_clock)

def start_clock():
    my_minutes_label

def stop_clock():
    pass

def reset_clock():
    pass

my_window = Tk() # instantiate an instance of a window
my_window.geometry('660x440')
my_window.title("Clock")
my_window.config(background='black')
my_window.iconphoto(True,PhotoImage(file='image.png'))
my_window.resizable(False,False)
my_window.maxsize(660,440)
my_window.minsize(660,440)

my_time_clock_frame = Frame(my_window,relief=SUNKEN)

my_hours_frame = Frame(my_time_clock_frame,relief=SUNKEN)
my_hours_label = Label(my_hours_frame,text='00:',font=('Consolas',23,'bold'),bg='black',fg='white')
my_hours_label.pack()

my_minutes_frame = Frame(my_time_clock_frame,relief=SUNKEN)
my_minutes_label = Label(my_minutes_frame,text='00:',font=('Consolas',23,'bold'),bg='black',fg='white')
my_minutes_label.pack()

my_seconds_frame = Frame(my_time_clock_frame,relief=SUNKEN)
my_seconds_label = Label(my_seconds_frame,text='00',font=('Consolas',23,'bold'),bg='black',fg='white')
my_seconds_label.pack()

my_time_clock_button_frame = Frame(my_window,relief=SUNKEN)
my_start_button = Button(my_time_clock_button_frame,text='Start',command=start_clock).pack(side=LEFT,anchor=NW)
my_reset_button = Button(my_time_clock_button_frame,text='Reset',command=reset_clock).pack(side=LEFT,anchor=NW)
my_stop_button = Button(my_time_clock_button_frame,text='Stop',command=stop_clock).pack(side=LEFT,anchor=NW)

my_clock_frame = Frame(my_window,relief=SUNKEN)
my_clock_label = Label(my_clock_frame,text='',font=('Consolas',12,'bold'),bg='black',fg='white')
my_clock_label.pack()
update_clock()

my_hours_frame.pack(side=LEFT,anchor=NW)
my_minutes_frame.pack(side=LEFT,anchor=NW)
my_seconds_frame.pack(side=LEFT,anchor=NW)
my_time_clock_frame.pack(side=TOP,padx=20,pady=20)
my_time_clock_button_frame.pack(side=TOP,padx=20,pady=20)
my_clock_frame.pack(side=TOP,padx=20,pady=20)
my_clock_frame.pack(side=TOP,padx=20,pady=20)

my_window.mainloop() # will place window on computer screen and will listen to events
