#!/usr/bin/python3

from modules.my_modules import *
from math import pi


squares = []
for x in range(1,10):
    squares.append(x**2)

print(hr,squares,hr)
del squares[:]

squares = list(map(lambda x: x**2, range(1,10)))

print(squares,hr)
del squares[:]

squares = [x**2 for x in range(1,10)]

print(squares,hr)
del squares[:]


combs = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combs,hr)
del combs[:]

for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs[len(combs):] = (x,y),

print(combs,hr)
del combs[:]

for i in [[x*2,x*-2] for x in range(8)]:
    combs[len(combs):] = i

print((sorted_combs := sorted(set(combs))),hr)
del combs[:]

for i in [x for x in sorted_combs if x < 0]:
    print("\tless than 0:",i)
print(hr)

for i in [x for x in sorted_combs if x > 0 or x == 0 and x >= 0]:
    print("\tgreater than or equal to 0:",i)
print(hr)

for i in [[abs(x)] for x in sorted_combs if x != 0]:
    combs[len(combs):] = i
print(set(combs),hr)
del combs[:]

for i in [[abs(x)] for x in sorted_combs if x != 0]:
    combs[len(combs):] = i
print(combs[::2],hr)
del combs[:]

combs = [weapon.strip() for weapon in ["     oryx","bat      ","mouse","      panda","       dormouse","woodchuck","octopus      ","pig","      jackal","opossum"]]
print(combs,hr)
del combs[:]

print(my_animal_lists(),hr)

combs = [str(round(pi,i)) for i in range(6)]
print(combs,hr)
del combs[:]

matrix = [
    [a for a in range(1,25) if a % 2 == 0],
    [b for b in range(1,25) if b % 3 == 0],
    [c for c in range(1,25) if c % 5 == 0],
    [d for d in range(1,25) if d % 7 == 0 ],
]

print(matrix,hr)

print([[rows[i] for rows in matrix] for i in range(3)],hr)

for i in range(3):
    combs[len(combs):] = [[rows[i]] for rows in matrix]

print(combs,hr)
del combs[:]

for row in matrix:
    combs.append(row)

print(combs,hr)
del combs[:]
del matrix[:]

matrix = (1,5,9),(2,6,10),(3,7,11),(4,8,12)

print(matrix,hr)
print(list(zip((1,5,9),(2,6,10),(3,7,11),(4,8,12))),hr)
del matrix

combs = [x**2 for x in range(1,23)]
print(combs,hr)
del combs[::2]
print(combs,hr)
del combs[0:4:2]
print(combs,hr)

my_tuple = tuple(x**2 for x in range(1,23))
print(my_tuple,hr)

# squence unpacking
a = b = c = my_tuple

print("\ta,b and c share memory location:",a is b is c,hr)
my_tuple = a,b,c
print(my_tuple,hr)
del my_tuple
del combs
del squares

print([x for x in 'ahracadahra' if x not in 'abc'],hr)

my_animals = dict(enumerate(my_animal_lists()))
print(my_animals,hr)

animals = my_animals.copy()
print(tuple(animals.keys()),hr)
print(tuple(animals.values()),hr)
print(tuple(animals.items()),hr)

print(squares := {"{} ** {}".format(x,x): x ** 2 for x in range(1,13)},hr)

for k,v in squares.items():
    print(k,"=",v)
print(hr)

for k,v in squares.items().__reversed__():
    print(k,"=",v)
print(hr)

for  i in reversed(range(1,21,2)):
    print(i)
print(hr)

for i in sorted(my_animal_lists()):
    print(i)
print(hr)

del animals
animals = my_animal_lists()

for i in animals[:]:
    animals.insert(0,i)
    print(i,len(i))
