#!/usr/bin/python3
from math import *

square = lambda x: pow(x, 2)
cube = lambda x: pow(x, 3)
power = lambda x,y: [pow(x, y) for x,y in range(1,x)]

def foreach(func,*args):
    for index in range(1,args[0]+1):
        if len(args) == 1:
            print(func(index))
        else:
            print(func(index,*args))


foreach(square,5)
foreach(cube,5)
foreach(power,5,5)
