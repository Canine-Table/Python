#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

# listbox
# a listing of selectable text items within it's own container

from tkinter import *

def submited():
    try:
        for i in my_listbox.curselection():
            print(my_listbox.get(i))
    except TclError:
        pass

def deleted():
    try:
        for i in my_listbox.curselection():
            my_listbox.delete(i)
    except TclError:
        pass

def added():
    my_listbox.insert(my_listbox.size(),my_entry.get())

my_window = Tk() # instantiate an instance of a window
my_window.geometry('420x420')
my_window.title("window title")
my_window.config(background='black')
my_window.iconphoto(True,PhotoImage(file='image.png'))

my_listbox = Listbox(my_window,
    bg='#F7FFDE',
    fg='#000000',
    font=('Constantia',24),
    selectbackground='black',
    selectforeground='white',
    selectmode=MULTIPLE,
)

my_button = Button(my_window,
    command=submited,
    text='Submit',
)

my_add_button = Button(my_window,
    command=added,
    text='Add Item',
)

my_delete_button = Button(my_window,
    command=deleted,
    text='Delete Item',
)

my_entry = Entry(my_window,

)

my_button.pack()
my_add_button.pack()
my_delete_button.pack()
my_entry.pack()
my_listbox.pack()

count = 1
for i in ['a','b','c','d','e','f','g']:
    my_listbox.insert(count,i)
    count += 1

my_window.mainloop() # will place window on computer screen and will listen to events