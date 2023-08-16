#!/usr/bin/python3
import time
from datetime import datetime

def pretty_output(function):
    def spacer():
        print('----------------------------------')

    def wrapper():
        print('\n\n\n')
        spacer()
        function()
        spacer()
    return wrapper


def execute_x_times(x):
    def execute_x(function):
        def wrapper():
            for i in range(x):
                function()
                print('Loop Count:',i)
        return wrapper
    return execute_x

def time_stamp(function):
    def wrapper():
        start_time = time.time()
        function()
        print('Time Stamp:',time.time() - start_time)
    return wrapper

def decorator(function):
    def wrapper():
        print('decoration begins')
        function()
        print('decoration ends')
    return wrapper


@execute_x_times(3)
@pretty_output
@time_stamp
@decorator
def func():
    print('hello')
    time.sleep(1)

func()

# func = decorator(func)
# or
# @decorator

def repetiton(counter):
    def decorator(function):
        def wrapper():
            for i in range(counter):
                function()
        return wrapper
    return decorator

def params(*args,**kwargs):
    def decorator(function):
        def wrapper():
            function(*args,**kwargs)
        return wrapper
    return decorator

def get_date(function):
    def wrapper():
        print(datetime.now())
        function()
    return wrapper

@pretty_output
@get_date
@repetiton(3)
@params('ball','car','far',first_name='John',last_name='doe',age=33)
def func_parameter(*args,**kwargs):
    for i,arg in enumerate(args):
        print('arg number',str(i+1)+':',arg)
    for k,v in kwargs.items():
        print('\nkey:',k,'\nvalue:',v)

func_parameter()



class Generic():

    def __init__(self):
        self._x = 10

    @property
    def x(self):
        print('getattr')
        return self._x

    @x.setter
    def x(self,value):
        print('setattr')
        self._x = value

    @x.deleter
    def x(self):
        print('delattr')
        del self._x


generic = Generic()

print(generic.x)
generic.x = 7
print(generic.x)
del generic.x
