#!/usr/bin/python3

# exception
# events detected during execution that interrupt the flow of a program

try:
    numerator = int(input('enter your numerator: '))
    denominator = int(input('enter your denominator: '))
except ZeroDivisionError as e:
    print("ZeroDivisionError Caught:",e)
except ValueError as e:
    print("ValueError Caught:",e)
except Exception:
    pass
else:
    print(numerator/denominator)