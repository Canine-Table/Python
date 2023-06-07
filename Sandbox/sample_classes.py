#!/usr/bin/python3
from modules.my_modules import *
import modules.class_modules as cm
from dataclasses import dataclass
from math import pi,sin

spam = []

class TestClass:
    """A Simple Example class"""
    integer = 1234567890
    def f(self):
        return "hello world"

test = TestClass()
print(hr,test.f())
print(test.integer)
print(test.__doc__,hr)
del test

class Complex:
    def __init__(self,realtime,imagpart):
        self.r = realtime
        self.i = imagpart

comp = Complex(3.0,-4.5)

print(comp.r,comp.i,hr)

comp.instance_object = 1

while comp.instance_object < 10:
    comp.instance_object = comp.instance_object * 2
print(comp.instance_object,hr)
del comp.instance_object
del comp

class Dog:
    def __init__(self,name):
        self._name = name
        self._tricks = []

    def add_trick(self,trick):
        self._tricks.append(trick)
        return self


fido = Dog("Fido")
buddy = Dog("Buddy")

fido.add_trick('roll over')
buddy.add_trick('play dead')
print("\n\tFido: {}\n\tBuddy: {}\n".format(fido._tricks,buddy._tricks),hr)
del fido
del buddy

def f1(self,x,y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return "hello world"
    h = g

c = C()
print(f1(c,4,4),hr)
del c

class Bag:
    def __init__(self):
        self.data = []

    def add_item(self,item):
        self.append(item)

    def add_item_twice(self,item):
        self.append(item)
        self.append(item)

print("bool is a subclass of int:",issubclass(bool,int),hr)
print("int is a subclass of float:",issubclass(int,float),hr)

class Mapping:
    def __init__(self,iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self,iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update # private copy of original update()

class MapSubclass(Mapping):
    def update(self, keys,values):
        for item in zip(keys,values):
            self.items_list.append(item)

my_list = []
msc = MapSubclass(my_list)

msc.update("a","b")
msc.update("abc","def")
print(msc.items_list)

mp = Mapping(my_list)

mp.update("ghijklmno")

print(mp.items_list)
print(my_list,hr)
del mp,msc

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

john = Employee("John","computer lab",1000)

print(john.name,john.dept,john.salary,hr)
del john

string = 'abcdefg'
it = iter(string)
print(it)

while True:
    try:
        print(next(it))
    except StopIteration:
        print(hr)
        break

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self,data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            print("completed",hr)
            raise StopIteration
        self.index = self.index -1
        return self.data[self.index]

spam.append("abcdefg")
rev = Reverse(spam)


print(rev.__doc__)
iter(rev)
for char in rev:
    print(char)


# generator expressions

def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]
    del index

for char in reverse("some world to yield"):
    print(char)
print(hr)
del char

print(sum(i*i for i in range(10)),hr)

xvec = [10,20,30]
yvec = [7,5,3]
print(sum(x*y for x,y in zip(xvec,yvec)),hr)
del yvec,xvec

sine_table = {x: sin(x*pi/180) for x in range(91)}
print(sine_table,hr)
del sine_table

data = 'golf'
print(list(data[i] for i in range(len(data)-1,-1,-1)),hr)
