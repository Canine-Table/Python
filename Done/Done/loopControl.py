#!/usr/bin/python3

# Loop Control
# break = used to terminate a loop entirely
# continue = skips to the next iteration of the loop
# pass = dpes nothing, acts as a placeholder

name = ""
while name == "":
    name = input("enter your name: ")
    if name == 'b':
        break
    elif name == 'c':
        pass
    elif name.__len__() <= 2:
        name = ""
        continue
