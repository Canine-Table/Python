#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

# canvas
# widget that is used to draw simple graphs, plots, images, etc in a window.

from tkinter import *

my_window = Tk() # instantiate an instance of a window
my_window.geometry('420x420')
my_window.title("window title")
my_window.config(background='black')
my_window.iconphoto(True,PhotoImage(file='image.png'))

my_canvas = Canvas(my_window)
my_canvas.create_line(0,0,100,100,fill='blue',width=400)
my_canvas.create_rectangle(50,50,500,500,fill='green',width=50,outline='purple')
my_canvas.create_polygon(100,100, 125,150, 50,75, 20,25, 250,275, 500,500,fill='yellow')
my_canvas.create_arc(500,500,0,0,fill='pink',style=CHORD,start=180)
my_canvas.create_arc(500,500,50,50,fill='orange',start=260)
my_canvas.create_arc(500,500,100,100,fill='red',start=180)
my_canvas.create_arc(500,500,150,150,fill='pink',style=CHORD)
my_canvas.create_arc(500,500,200,200,fill='orange',start=90)
my_canvas.create_arc(500,500,250,250,fill='red',style=PIESLICE,start=90)
my_canvas.create_arc(500,500,300,300,fill='pink',style=CHORD,start=260)
my_canvas.create_arc(500,500,800,800,fill='brown',extent=260)
my_canvas.create_arc(500,500,800,800,fill='indigo',start=260,extent=120)
my_canvas.create_arc(500,500,800,800,fill='pink',extent=60)
my_canvas.create_arc(500,500,800,800,fill='green',start=40,extent=40)
my_canvas.create_arc(500,500,800,800,fill='lime',start=80,extent=30)
my_canvas.create_arc(500,500,800,800,fill='beige',start=90,extent=10)
my_canvas.create_arc(500,500,800,800,fill='yellow',start=100,extent=80)
my_canvas.create_arc(700,100,100,700,fill='orange',start=260)
my_canvas.pack(expand=True,fill=BOTH,padx=1,pady=1)

my_window.mainloop() # will place window on computer screen and will listen to events