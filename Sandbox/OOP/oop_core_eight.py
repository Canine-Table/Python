#!/usr/bin/python3
from oop_modules.others.core import (
    Core,
    DunderCore,
    DunderDictCore,
    DunderListCore,
)


def my(number: int =15,symbol: str = '='):
    s: str = ''
    while len(s).__lt__(number):
        s+=symbol
    print('\n\n',s,'\n\n')

my(75,'\/')
Core(5,45).addition()
Core(50,545).subtraction()
Core(16,15).modulus()
Core(9,9).multiplication()
Core(5,505).division()
Core(3.14195).round()
Core(3.14195).ceiling()
Core(3.14195).floor()
Core(-314195).absolute()
Core(5,5).power()
Core(True,False).xor()
Core(3,5).ls()
Core(38,5).rs()
Core([5,6,7,8],[9,10,11,12]).addition()
Core([5,6,7,8],[9,10,11,12]).merge()
my(75,'+-')
x = DunderCore([535,36,37,83])
y = DunderCore([89,410,311,312])
z = x + y
z = x - y
z = x / y
z = x * y
my(75,'*%')

dd = DunderDictCore()
dd['one'] = 1
dd['two'] = 2
dd['three'] = 3

for k,v in dd.items():
    print(k,v)

my(75,')(')

ll = DunderListCore(['a','a','a','a'])
ll[4] = 'abc123'
ll[3]
for l in ll:
    print(l)
del ll[4]
