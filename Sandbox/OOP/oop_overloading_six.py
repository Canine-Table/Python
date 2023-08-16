#!/usr/bin/python3

from oop_modules.others.overloading import (
    GetSetList,
    GetSetInt
)

a = GetSetInt(3234)
b = GetSetInt('3234')

print(a.val)
print(b.val)

c = GetSetList(['34',3,'56'])
d = GetSetList(('34',3,'56'))

print(c.val)
print(d.val)

d.doc = 'string'
print(d.doc)
d.doc = 3.14195
print(d.doc)
