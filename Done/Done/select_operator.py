#!/usr/bin/python3

def check_operator(operator):
    try:
        if operator == '*':
            return "Multiplication"
        elif operator == '/':
            return "Division"
        elif operator ==  '+':
            return "Addition"
        elif operator ==  '-':
            return "Subtraction"
        else:
            raise Exception('invalid') # raise an Exception with the message 'invalid' after invalid user input is recived
    except Exception as e:
        return (e).__str__()

print(check_operator(input("enter an operator: ")))

print('Thank you')
