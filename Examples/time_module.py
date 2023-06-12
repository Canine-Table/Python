#!/usr/bin/python3

# time.ctime(0)
# convert a time expressed in seconds since the epoch to a readable string

# epoch
# when your computer thinks time began (reference point)

from time import *

print(ctime(time()))
print(ctime())
print(time())
print(localtime())
print( local_time := strftime('%B %d %Y %H:%M:%S',localtime()))
print( time_string := strptime('20 April, 2020','%d %B, %Y'))

# (year, month, day, hours, minuutes, seconds, #days of the week, $days of the year, dst)
print(time_tuple := asctime(tmp := (2022, 4, 20, 4, 20, 2, 2, 3, 4)))
print(seconds_since_epoch := mktime(tmp))