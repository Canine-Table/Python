#!/usr/bin/python3

from oop_modules.animals.cat import Cat
from oop_modules.animals.dog import Dog

dog1 = Dog(name='Rover')
cat1 = Cat(name='Fluffy')

dog1.fetch(thing='stick').sleep()
cat1.swat(action='shreds',thing='string').eat()
