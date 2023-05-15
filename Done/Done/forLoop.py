#!/usr/bin/python3

# for loop
# a statement that will execute it's block of code a limited number of times.
#
#       while loop = unlimited
#       for loop = limited

import time

for i in range(10):
    print(i+1)

for j in range(7,99,7):
    print(j)

for seconds in range(10,0,-1):
    time.sleep(1)
    print(seconds)
print("done")