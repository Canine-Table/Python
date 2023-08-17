#!/usr/bin/python3
from oop_modules.others.abstraction import ABCClass
from oop_modules.organism.species.coli import Coil
a = ABCClass()

b = Coil(name='Ralf',age=1,species='coil',common_name=44)
b._common_name = 5
print(b._common_name)
