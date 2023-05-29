#!/usr/bin/python3

# function written in 1 line using lambda keyword
# accepts any number of arguments but only has one expression
# like a shortcut (useful if needed for a short period of time, throw-away)

multiply = lambda x,y: print(x,'x',y,'=',x * y)
add = lambda x,y: print(x,'+',y,'=',x + y)
divide = lambda x,y: print(x,'/',y,'=',x / y)
age_check = lambda age:print('your old enough.') if age >= 18 else print('your to young.')
multiply(55,6)
add(3,3)
divide(32,32)
age_check(int(input('enter your age: ')))