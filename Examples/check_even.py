#!/usr/bin/python3

def is_even(number):
    if number % 2 == 0:
        return True
    return False

if is_even(number := int(input("enter a number: "))):
    print(number,"is an even number")
else:
    print(number,"is an odd number.")
