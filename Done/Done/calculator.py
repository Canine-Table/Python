#!/usr/bin/python3
# Program name: calulator.py
# Program purpose: calculator
# Author: Benjamin Stroobach-Wilson, 041048348, 23S_CST8245_010
# Date & version: Monday, May 15, 2023 3:08:17 PM version: 1.0
# Completion time: 45 minutes

import math
user_input = input("enter an equation to calculate: ").split(" ")
total = current_value = 0 # initialize total and current total to zero

def valid_operators(operator):
    # this function is for verifying if the operator of the equation if a valid math operator.
    match operator:
        case '+':
            pass
        case '-':
            pass
        case '*':
            pass
        case '/':
            pass
        case '^':
            pass
        case _:
            print(operator,"is not a valid math operator.")
            exit()

def power(value_1,value_2):
        # this function is used to add the power option to the Python script.
        return math.floor(math.pow(int(value_1),int(value_2)))

def calculate(value_1,operator,value_2):
    # this function is used to calulate the current equation.
    return eval(str(value_1) + str(operator) + str(value_2))

def print_output(value_1,operator,value_2,total_value):
    # this function is used to print out the current equation and value.
    print(str(value_1)+" "+str(operator)+" "+str(value_2)+" = "+str(total_value))

try: # all user input is DANGEROUS, catching these inputs that users may enter to try to break your code.
    while user_input != []: # checks if the Python script went through all the values the user entered.
        if current_value == 0: # if the current_value is 0 then this is the first loop which is relevant if multiple values are entered.
            valid_operators(user_input[1]) # checks the operator so the user wont break the Python script.
            if str(user_input[1]) == '^': # if the user enters the top hat as the operator, the power function will be executed instead of the default calculate function.
                total = power(user_input[0],user_input[2])
            else:
                total = calculate(user_input[0],user_input[1],user_input[2])
            print_output(user_input[0],user_input[1],user_input[2],total) # executes the print_output that prints the current values of the executed loop.
            current_value = total # updates the current_value to the previous total of the last loop.
            for i in range(3): # removes the values that the Python script has parsed.
                user_input.pop(0)
        else:
            valid_operators(user_input[0]) # checks the operator so the user wont break the Python script.
            if str(user_input[0]) == '^':
                total = power(current_value,user_input[1])
            else:
                total = calculate(current_value,user_input[0],user_input[1]) # updates the total value.
            print_output(current_value,user_input[0],user_input[1],total) # executes the print_output that prints the current values of the executed loop.
            current_value = total # updates the current_value to the previous total of the last loop.
            for j in range(2): # removes the values that the Python script has parsed.
                user_input.pop(0)
except (ValueError,ZeroDivisionError,IndexError,SyntaxError) as e: # handle errors because all user input should be considered dangerous code. e holds the error message.
    print("Invalid input or calculation error:", e)
finally: # after all code within the try block is complete, this section will finish the script.
    print("done") # to let the user know the program has completed execution
