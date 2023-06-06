#!/usr/bin/python3

import math

print("Squared Numbers")
for i in [x**2 for x in range(1,12)]:
    n = round(math.sqrt(i))
    print(n,"x",n,"=",i)

