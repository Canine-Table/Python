#!/usr/bin/python3

try:
    value1 = input("enter a number: ")
    value2 = input("enter another number: ")
    print(str(value1)+" + "+str(value2)+" = "+str(int(value1)+int(value2)))
except ValueError:
        try:
             print(str(value1)+" + "+str(value2)+" = "+str(float(value1)+float(value2)))
        except ValueError:
            print("enter numbers please")
        finally:
             print("converted to type float")
finally:
     print("done")