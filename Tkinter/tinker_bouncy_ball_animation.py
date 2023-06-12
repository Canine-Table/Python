#!/usr/bin/python3

# windows
# serves as a container to hold or contain these widgets
 
# widgets
# gui elements: buttons, textboxes, labels, images

from tkinter import *
from time import *
from multiprocessing import *
class Ball:

    def __init__(self,canvas,x_value,y_value,diameter,x_velocity,y_velocity,color):
        self._canvas = canvas
        self._x_value = x_value
        self._y_value = y_value
        self._diameter = diameter
        self._x_velocity = x_velocity
        self._y_velocity = y_velocity
        self._color = color
        self._image = self._canvas.create_oval(self._x_value,self._y_value,self._diameter,self._diameter,fill=self._color)
    
    def move_up_down(self):
        window_tk_y = int(str(my_window.winfo_geometry().split('x')[1]).split('+')[0])
        canvas_y = round(self._canvas.coords(self._image)[1])
        canvas_y_r = round(self._canvas.coords(self._image)[3])
        total_y=window_tk_y-canvas_y
        if canvas_y_r >= window_tk_y or total_y >= window_tk_y:
            self._y_velocity = -self._y_velocity
        self._canvas.move(self._image,0,self._y_velocity)
        self._canvas.update()
        return self

    def move_left_right(self):
        sleep(0.001)
        window_tk_x = int(my_window.winfo_geometry().split('x')[0])
        canvas_x = round(self._canvas.coords(self._image)[0])
        canvas_x_r = round(self._canvas.coords(self._image)[2])
        total_x=window_tk_x-canvas_x
        if canvas_x_r >= window_tk_x or total_x >= window_tk_x:
            self._x_velocity = -self._x_velocity
        self._canvas.move(self._image,self._x_velocity,0)
        self._canvas.update()
        return self

my_window = Tk() # instantiate an instance of a window
my_window.geometry('920x920')
my_window.title("Bouncing Balls")
my_window.config(background='black')
my_window.iconphoto(True,PhotoImage(file='image.png'))
my_canvas = Canvas(my_window)
my_canvas.pack(expand=True,fill=BOTH,padx=1,pady=1)

green_ball = Ball(my_canvas,100,100,200,10,10,'green')
blue_ball = Ball(my_canvas,500,500,300,15,15,'blue')
yellow_ball = Ball(my_canvas,200,200,300,5,5,'yellow')

def main():
    while True:
        yellow_ball.move_left_right().move_up_down()
        blue_ball.move_left_right().move_up_down()
        green_ball.move_left_right().move_up_down()

if __name__ == '__main__':
    main()

my_window.mainloop() # will place window on computer screen and will listen to events