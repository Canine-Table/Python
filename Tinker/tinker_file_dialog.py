#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

from tkinter import *
from tkinter import filedialog

def open_file():
    my_file_attribs = str(filedialog.askopenfile(
        initialdir='.',
        title='Open File Dialog',
        filetypes=(
            ('Python Files',"*.py"),
            ('Python Module Files',"*.mpy"),
            ('Text Files',"*.txt"),
        ))).split(' ')
    
    for i in my_file_attribs:
        if i == 'None':
            break
        print(i)

    try:
        open_file = open(my_file_attribs[1][6:-1],'r')
        print( my_text := open_file.read())
        my_text_area.insert(END,my_text)
        open_file.close()
    except IndexError:
        pass

def save_file():
    my_save_file = filedialog.asksaveasfile(
        defaultextension='.txt',
        initialdir='~/Downloads',
        filetypes=(
            ('Text Files','.txt'),
            ('Python FileS','.py'),
            ('Python Module Files','.mpy'),
            ('All Files','.*'))
        )

    try:
        my_save_file.write(str(my_text_area.get('1.0',END)))
        my_save_file.close()
    except AttributeError:
        pass


my_window = Tk() # instantiate an instance of a window
my_window.geometry('920x920')
my_window.title("window title")
my_window.config(background='black')
my_window.iconphoto(True,PhotoImage(file='image.png'))

my_ask_open_filename_button = Button(my_window,
    command=lambda : open_file(),
    text='Open File'
)

my_save_file_button = Button(my_window,
    command=lambda : save_file(),
    text='Save File',
)

my_text_area = Text(my_window,
    fg='white',
    bg='black',
    font=('Ink Free',12),
    padx=5,
    pady=5,
)



my_ask_open_filename_button.pack()
my_save_file_button.pack()
my_text_area.pack()
my_window.mainloop() # will place window on computer screen and will listen to events
