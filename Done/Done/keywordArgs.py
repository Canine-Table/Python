#!/usr/bin/python3

# Keyword Args
# arguments preceded by an identifier when passe ti a function
# the order of the arguments does not matter unlike positional args
# python knows the names of the args that our function receives

def name(first,last):
    full_name = first+" "+last
    return full_name
print('Name:',name(first="Canine",last="Table"))