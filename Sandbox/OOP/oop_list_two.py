#!/usr/bin/python3

from oop_modules.assignments import MaxSizeList


list_one = MaxSizeList(max=3)

list_one.push('1')
list_one.push('2')
list_one.push('3')
list_one.push('4')
list_one.push('5')
list_one.push('6')
list_one.push('7')

list_one.get_list()
