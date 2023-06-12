#!/usr/bin/python3

# reduce()
# apply a function to an iterable and reduce it to a single cumulative value
# performs function on first two elements and repeats process until 1 value remains 
# reduce(function, iterable)

import functools

letters = ['H','e','l','l','o',' ','w','o','r','l','d']
word = functools.reduce(lambda x, y,: x + y, letters)
print(word)
user_input = functools.reduce(lambda x,y:x + y, z := input('enter some words: ').split(' '))
print(user_input)
print(z)


string_num = list(map(int,str(input('string nums: ')).split(' ')))
num_add = functools.reduce(lambda x, y: x + y, string_num)
num_subtract = functools.reduce(lambda x, y: x - y, string_num)
print(num_add)