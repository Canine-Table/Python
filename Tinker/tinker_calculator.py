#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

from tkinter import *
from math import *
class Calculator():
    def __init__(self,window,symbol,rows,columns):
        self._symbol = symbol
        self._window = window
        self._rows = rows
        self._columns = columns
        self._button = Button(self._window,text=self._symbol,font=('Consolas',12,'bold'),command=lambda : send_input(self._symbol))
        self._button.grid(padx=10,pady=10,row=self._rows,column=self._columns)

def send_input(input):
    global boolean
    global user_input_text
    global power_me
    try:
        if input in ['0','1','2','3','4','5','6','7','8','9']:
            if boolean == False:
                boolean = True
            last = input
            user_input_text = user_input_text + str(input)
            user_input.set(user_input_text)
        elif input in ['/','*','-','+','.']:
            if boolean == True:
                user_input_text = user_input_text + str(input)
                user_input.set(user_input_text)
                boolean = False
        else:
            match input:
                case 'D':
                    user_input_text = user_input_text[0:-1]
                    user_input.set(user_input_text)
                case 'C':
                    user_input_text = ''
                    user_input.set(user_input_text)
                case '=':
                    total = str(eval(user_input_text))
                    user_input_text = total
                    user_input.set(total)
                case '√':
                    user_input_text = str(sqrt(eval(user_input_text)))
                    user_input.set(user_input_text)
    except SyntaxError:
        user_input.set('SyntaxError')
        user_input_text = ''
    except ZeroDivisionError:
        user_input.set('ZeroDivisionError')
        user_input_text = ''


my_window = Tk() # instantiate an instance of a window
my_window.title("Calculator")
my_window.maxsize(405,410)
my_window.minsize(405,410)
my_window.iconphoto(True,PhotoImage(file='image.png'))

user_input_text = ''
boolean = False
power_me = False

user_input = StringVar()
window_label = Label(my_window,height=2,textvariable=user_input,font=('Consolas',12,'bold'))
window_label.pack(fill=X)

my_button_frame = Frame(my_window,relief=SUNKEN,bg='gray')

one = Calculator(my_button_frame,'1',1,0)
two = Calculator(my_button_frame,'2',1,1)
three = Calculator(my_button_frame,'3',1,2)
four = Calculator(my_button_frame,'4',1,3)
five = Calculator(my_button_frame,'5',1,4)
six = Calculator(my_button_frame,'6',1,5)
seven = Calculator(my_button_frame,'7',2,0)
eight = Calculator(my_button_frame,'8',2,1)
nine = Calculator(my_button_frame,'9',2,2)
zero = Calculator(my_button_frame,'0',2,3)

plus = Calculator(my_button_frame,'+',2,4)
minus = Calculator(my_button_frame,'-',2,5)
square = Calculator(my_button_frame,'√',3,0)
divide = Calculator(my_button_frame,'/',3,1,)
multiply = Calculator(my_button_frame,'*',3,2)
dot = Calculator(my_button_frame,'.',3,3)
equal = Calculator(my_button_frame,'=',3,4)
clear = Calculator(my_button_frame,'C',3,5)
delete = Calculator(my_button_frame,'D',4,0)

my_button_frame.pack(fill=X,side=TOP)
my_window.mainloop() # will place window on computer screen and will listen to events