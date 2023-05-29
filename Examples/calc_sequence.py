#!/usr/bin/python3

print('Hello', first_name := input('enter your first name: '),'welcome to python.') # prompts the user for their first name.

def typecast_checker():
    try:
        my_first_floating_point_cast = float(input('enter a number: '))
        my_second_floating_point_cast = float(input('enter another number: '))

        return'First float: {}\nSecond float: {}\n'.format(
            my_first_floating_point_cast,
            my_second_floating_point_cast
        )

    except Exception as e:
        
        return type (e).__name__

print(typecast_checker()) # asks for 2 numbers and returns either an error or the 2 valid values. 
# the typecast_checker function

def calculation_checker():
    try:
        first_value = int(input('enter your first value: '))
        second_value = int(input('enter your second value: '))
        sum = float(first_value + second_value)
        difference = float(first_value - second_value)

    except Exception as e:

        return type (e).__name__

    finally:

        return 'the sum of {0} + {1} is {2}\nthe difference of {0} - {1} is {3}\nThank you and goodbye {4}.'.format(
            float(first_value),
            float(second_value),
            sum,
            difference,
            first_name
        )

print(calculation_checker())
