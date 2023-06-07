#!/usr/bin/python3

def add_numbers(num_1,num_2):
    return num_1 + num_2

num_1 = int(input("enter your first number: "))
num_2 = int(input("enter your second number: "))

print("the total of",num_1,"+",num_2,"=",add_numbers(num_1,num_2))
