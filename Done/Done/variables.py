#!/usr/bin/python3

# variables
# a container of a value
# Behaves as the value that is contains

greet, first_name, last_name, my_age, boolean_value, floating_point, t, v = \
str("hello world"), \
str("John"), \
str("Doe"), \
int(33), \
bool(True), \
float(3.14195), \
str("\nType: "), \
str("\tValue: ")

print(t+str(type(my_age))+v+str(my_age)+t+\

str(type(greet))+v+str(greet)+t+\
str(type(first_name))+v+str(first_name)+t+\
str(type(last_name))+v+str(last_name)+t+\
str(type(boolean_value))+v+str(boolean_value)+t+\
str(type(floating_point))+v+str(floating_point))

# multiple assignment
# allows us to assign multiple variables at the same time in one line of code
Spongebob = Sandy = Patrick = Squidward = 30
print("\nTotal Value: "+str(int(Spongebob+Patrick+Sandy+Squidward)))