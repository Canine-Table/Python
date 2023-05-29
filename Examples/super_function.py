#!/usr/bin/python3

# super()
# function used to give access to the methods of a parent class.
# returns a temporary object of a parent class when used

class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    pass
    def area(self):
        return(self.length*self.width)

class Cube(Rectangle):
    
    def __init__(self, length, width, hight):
        super().__init__(length, width)
        self.hight = hight

    def volume(self):
        return(self.length*self.width*self.hight)

cube = Cube(4,4,4)
print(cube.volume())

square = Square(6,6)
print(square.area())