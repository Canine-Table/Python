#!/usr/bin/python3

# *Args
# parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments

def add(*args):
    sum = 0
    for i in args:
        sum += i
    stuff = list(args)
    stuff[0] = 9
    for j in stuff:
        sum += j
    return sum
print(add(2,3,4,5,3,2,4,5))