#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

from tkinter import *
from tkinter import filedialog

def open_file():
    my_file_path = filedialog.askopenfilename(
        initialdir='.',
        title='Open File Dialog',
        filetypes=(
            ('Python Files',"*.py"),
            ('Python Module Files',"*.mpy"),
            ('Text Files',"*.txt"),
            ('All Files',"*.*"),
        ))

    try:
        my_file = open(my_file_path,'r')
        my_text_area.insert(END,my_file.read())
        my_file.close()
    except (TypeError,FileNotFoundError):
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
my_window.geometry('420x420')
my_window.title("window title")
my_window.config(background='black')
my_window.iconphoto(True,PhotoImage(file='image.png'))

my_menu_bar = Menu(my_window,

)

my_file_menu = Menu(my_menu_bar,
    tearoff=0,
)

my_file_menu.add_command(
    label='Open',
    command=open_file,
)

my_file_menu.add_command(
    label='Save As',
    command=save_file,
)

my_file_menu.add_separator()

my_file_menu.add_command(
    label='Exit',
    command=exit,
)

my_menu_bar.add_cascade(
    label='File',
    menu=my_file_menu,
)


my_editor_menu = Menu(my_menu_bar,
    tearoff=0,
)

my_menu_bar.add_cascade(
    label='Edit',
    menu=my_editor_menu,
)


my_editor_menu.add_command(
    label='Copy',
    command=lambda : print('copy')
)

my_editor_menu.add_command(
    label='Cut',
    command=lambda : print('cut')
)

my_editor_menu.add_command(
    label='Paste',
    command=lambda : print('paste')
)

my_text_area = Text(my_window,
    fg='white',
    bg='black',
    font=('Ink Free',12),
    padx=10,
    pady=10,
)

my_text_area.pack(expand=True,fill=BOTH)
my_window.config(menu=my_menu_bar,padx=5,pady=15)
my_window.mainloop() # will place window on computer screen and will listen to events