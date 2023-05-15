#!/usr/bin/python3
input = input("enter an equation to calculate: ")
user_input = input.split(" ")
total = current_value = 0 # initialize total and current total to zero
try:
    while user_input != []:
        if current_value == 0:
            total = eval(str(user_input[0]) + str(user_input[1]) + str(user_input[2]))
            print(str(user_input[0])+" "+str(user_input[1])+" "+str(user_input[2])+" = "+str(total))
            current_value = total
            for i in range(3):
                user_input.pop(0)
        else:
            total = eval(str(current_value) + str(user_input[0]) + str(user_input[1]))
            print(str(current_value)+" "+str(user_input[0])+" "+str(user_input[1])+" = "+str(total))
            current_value = total
            for j in range(2):
                user_input.pop(0)
except (ValueError,ZeroDivisionError,IndexError,SyntaxError) as e: # handle errors because all user input should be considered dangerous code.
    print("Invalid input or calculation error:", e)
finally:
    print("done")