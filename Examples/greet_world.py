#!/usr/bin/python3

my_name = user_name = 'u8245' # string
num1 = 3 # number
num2 = 1.5 # float

# str.format
# optional methods that give users 
# more control when displaying output

def get_number(value): # this is a function that accepts 1 argument which is gathered from line 33
    try: # to catch users trying to break the logic of the code
        return f'String Replication: {value * 2}\nMultiplication: {int(value) * 2}' # this returns an f-string or 
            # a 'formated string literal'. An f-string is a way to embed expressions or variables within a string 
            # using {curly braces}. the return keyword makes this function act as like a variable that holds the value
            # f'String Replication: {value * 2}\nMultiplication: {int(value) * 2}' if the condition is true.
    except (Exception) as e: # if the user breaks the logic 'in this case if they enter a non numeric value' 
        # the error will be caught by Exception class and stored in the variable called e
        return f'Error type: "{type (e).__name__}"' # the return keyword is a self explanitory keyword, it returns the value
            # provided and any code after the keyword will be ignored. the e variable is part of a the class Exception, this
            # class has many methods, one of its methods is __name__ which retrives the name of the error that occured.
            # this is then returned making the function act as a variable holfing the value f'Error type: "{type (e).__name__}"'

print_message = '''Hello World!
My name is {} and your name is {}.
The value of num1 is: {} and the value of num2 is: {}
{}
'''.format( # the format() method is one of the methods python provides to strings.
my_name, # puting these values on a new line is common practice for readability
user_name,
num1,num2,
get_number(input('enter a number: '))
) # curly braces are used as placeholders for the format method. by default the number of curly brace pairs in a string
# must has a matching number of values within the .format() method.

print(print_message)
