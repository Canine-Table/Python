#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

from tkinter import *

count = 5
def submit_button():
    global count
    if count != 0:
        count -= 1
    else:
         my_entrybox.config(
              state=DISABLED,
         )

    print(username := my_entrybox.get())

def delete_button():
    my_entrybox.delete(0,END)

def backspace_button():
        my_entrybox.delete(len(my_entrybox.get())-1,END)

my_window = Tk() # instantiate an instance of a window
my_window.geometry('820x820')
my_window.title("window title")
my_window.config(background='black')
my_image = PhotoImage(file='image.png')
my_window.iconphoto(True,my_image)

my_entrybox = Entry(my_window,
    font=('Arial,',24,'bold'),
    fg='yellow',
    bg='gray',
    show='*',
)

my_submit_button = Button(my_window,
    font=('Arial,',24,'underline'),
    text='Submit',
    padx='10',
    pady='5',
    command=submit_button,
)

my_delete_button = Button(my_window,
    font=('Arial,',24,'underline'),
    text='Delete',
    padx='10',
    pady='5',
    command=delete_button,
)

my_backspace_button = Button(my_window,
    font=('Arial,',24,'underline'),
    text='Backspace',
    padx='10',
    pady='5',
    command=backspace_button,
)

my_entrybox.insert(0,'Some Text')
my_entrybox.pack(
    side=TOP,
)

my_submit_button.pack(
    side=BOTTOM,
)

my_delete_button.pack(
    side=BOTTOM
)

my_backspace_button.pack(
    side=BOTTOM
)

my_window.mainloop() # will place window on computer screen and will listen to events