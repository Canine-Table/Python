#!/usr/bin/python3

# Splicing
# create a subscring by extracting elements from another string
#   indexing[] or slice()
#   [start:stop:step]
# the first index 'start' is inclusive, 'stop' is exclusive

my_string = "Bro Code is a great youtuber"
youtuber = my_string[:8]
rest_of_string = my_string[9:]
step = my_string[::2]
reversed_string = my_string[::-1]
print(my_string)
print(youtuber)
print(rest_of_string)
print(step)
print(reversed_string)