#!/usr/bin/python3

# if statement
# a block of code that will execute if it's condition is true.

try:
    age = int(input("How old are you: "))
    if age > 18 and age < 130:
        print("you are an adult.")
    elif age <= 0:
        print("you have not been born yet.")
    elif age == 18:
        print("welcome to the age of responsibilities.")
    elif age >= 130:
        print("you are very dead.")
    else:
        print("you are a child")
except ValueError:
    print("please enter a valid age.")