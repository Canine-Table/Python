#!/usr/bin/python3

# logical operators (and,or,not)
# used to check if two or more conditions statements.

temp = 20
sunny = True

if temp <= 0 or temp >= 30:
    print("The temperature is bad")
else:
    print("The temperature is good")

if not sunny:
    print("It is cloudy")
else:
    print("It is sunny")