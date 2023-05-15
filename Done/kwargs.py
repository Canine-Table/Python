#!/usr/bin/python3

# **Kwargs (or key word args)
# parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varrying amount of keyword arguments

def hello_world(**kwargs):
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")
    print()
hello_world(title="Mr.",first='John',last="Doe")
hello_world(title="Mrs.",first='Jane',last="Doe")
hello_world(first='Canine',last="Table")