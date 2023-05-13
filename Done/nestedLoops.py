#!/usr/bin/python3

# nested functions
# the "inner loop" will finish all of its iterations
# before finishing one iteration of the "outer loop"

rows = input("enter the number of rows: ")
columns = input("enter the number of columns: ")
symbol = input("enter the symbol to print: ")

for i in range(int(rows)):
    for j in range(int(columns)):
        print(symbol, end="")
    print()