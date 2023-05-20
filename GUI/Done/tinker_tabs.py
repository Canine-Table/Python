#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

from tkinter import *
from tkinter import ttk

my_window = Tk() # instantiate an instance of a window
my_window.geometry('420x420')
my_window.title("window title")
my_window.config(background='black')
my_window.iconphoto(True,PhotoImage(file='image.png'))

my_note_book = ttk.Notebook(my_window
)

my_tab_0 = Frame(my_note_book,
    bg='pink',
)

my_tab_1 = Frame(my_note_book,
    bg='red',
)

my_tab_2 = Frame(my_note_book,
    bg='blue',
)

my_tab_3 = Frame(my_note_book,
    bg='orange',
)

my_tab_4 = Frame(my_note_book,
    bg='yellow',
)

my_tab_5 = Frame(my_note_book,
    bg='green',
)

Label(my_tab_0,text='Some Text for this Label in tab number 0.').pack()
Label(my_tab_1,text='Some Text for this Label in tab number 1.').pack()
Label(my_tab_2,text='Some Text for this Label in tab number 2.').pack()
Label(my_tab_3,text='Some Text for this Label in tab number 3.').pack()
Label(my_tab_4,text='Some Text for this Label in tab number 4.').pack()
Label(my_tab_5,text='Some Text for this Label in tab number 5.').pack()


my_note_book.add(my_tab_0,text='Tab 0')
my_note_book.add(my_tab_1,text='Tab 1')
my_note_book.add(my_tab_2,text='Tab 2')
my_note_book.add(my_tab_3,text='Tab 3')
my_note_book.add(my_tab_4,text='Tab 4')
my_note_book.add(my_tab_5,text='Tab 5')
my_note_book.pack(expand=True,fill=BOTH)

my_window.mainloop() # will place window on computer screen and will listen to events
