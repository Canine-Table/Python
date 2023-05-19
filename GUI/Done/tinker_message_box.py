#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

from tkinter import *
from tkinter import messagebox # import the message box lib

show_message = lambda : messagebox.showinfo(title='info',message='hello world',icon='info')
show_warning = lambda : messagebox.showwarning(title='WARN',message='you have a WARNING MESSAGE!',icon='warning')
show_error = lambda : messagebox.showerror(title='err',message='you have a ERROR MESSAGE!',icon='error')

def show_ask_ok():
    if messagebox.askyesno(title='yes/no',message='yes or no?'):
        print('you said yes :)')
    else: 
        print('you said no :(')

def show_ask_cancel():
    if messagebox.askokcancel(title='ok/cancel',message='ok or cancel?'):
        print('you said yes :)')
    else: 
        print('you said no :(')

def show_ask_question():
    if messagebox.askquestion(title='question',message='asking a question?') == 'yes':
        print('you said yes :)')
    else:
        print('you said no :(')

def show_retry_cancel():
    if messagebox.askretrycancel(title='retry/cancel',message='asking a question?'):
        print('you said retry :)')
    else:
        print('you said cancel :(')


def show_yes_no_cancel():
    match messagebox.askyesnocancel(title='yes/no/cancel',message='asking a question?',icon='question'):
        case True:
            print('you said yes :)')
        case False:
            print('you said no :(')
        case None:
            print('you said cancel :o')


my_window = Tk() # instantiate an instance of a window
my_window.geometry('420x420')
my_window.title("window title")
my_window.config(background='black')
my_window.iconphoto(True,PhotoImage(file='image.png'))

show_message_button = Button(my_window,
    text='show message',
    command=show_message,
)

show_warning_button = Button(my_window,
    text='show warning',
    command=show_warning,
)

show_error_button = Button(my_window,
    text='show error',
    command=show_error,
)

show_ask_ok_button = Button(my_window,
    text='show ok',
    command=show_ask_ok,
)

show_ask_cancel_button = Button(my_window,
    text='show cancel',
    command=show_ask_cancel,
)

show_ask_question_button = Button(my_window,
    text='show question',
    command=show_ask_question,
)

show_yes_no_cancel_button = Button(my_window,
    text='show yes, no, cancel',
    command=show_yes_no_cancel,
)

show_retry_cancel_button = Button(my_window,
    text='show retry, cancel',
    command=show_retry_cancel,
)

show_message_button.pack()
show_warning_button.pack()
show_error_button.pack()
show_ask_cancel_button.pack()
show_ask_ok_button.pack()
show_ask_question_button.pack()
show_retry_cancel_button.pack()
show_yes_no_cancel_button.pack()

my_window.mainloop() # will place window on computer screen and will listen to events
