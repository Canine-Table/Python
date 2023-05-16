#!/usr/bin/python3

# Scope
# the region that a variable is recognized
# a variable is only avalible from inside the region it was created
# a global and locally scoped versions of a variable can be created

# L = Local
# E = Enclosing
# G = Global
# B = Built-in

name = 'John Doe'
def display_name():
    name = 'Canine Table'
    print(name)
display_name()
print(name)