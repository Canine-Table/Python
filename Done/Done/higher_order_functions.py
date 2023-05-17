#!/usr/bin/python3

# Higher Order Functions
# a function that either:
#   1.) accepts a function as an argument
#   2.) returns a function (in Python, functions are also treated as objects)

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def echo(func):
    print(text := func(input('enter some text: ')))

echo(loud)
echo(quiet)

def divisor(x):
    def dividend(y):
        return x / y
    return dividend

div = divisor(20)
print(div(10))