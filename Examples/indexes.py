#!/usr/bin/python3

# index operator []
# gives access to a sequence's element (str,list,tuples)

name = 'canine table'
if name[0].islower():
    last = name[7:].capitalize()
    first = name[0:6].capitalize()
    full = name[0::].upper()
    skip_two = name[::2].upper()
    print(skip_two)
    skip_two = name[::-2].upper() 
    print(skip_two)
    print(full)
    print(first,last)
