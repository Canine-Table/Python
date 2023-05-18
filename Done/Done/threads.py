#!/usr/bin/python3

# Threads
# a flow of executon. Like a separate order of instructions.
# However each thread takes a turn running to achieve concurrency
# GIL = (global interptreter lock),
# allows onlu one thread to hold control of the Python interpreter

# cpu bound
# program/task sspends most of it's time waiting for internal events (CPU interupts)
# use multiprocessing

# I/O bound
# program/task spends most of it's time waiting for external events (user input) 
# use multithreading

from threading import *
from time import *

def sleeping(num):
    sleep(num)
    print('sleep is done')
    x.start()
    y.start()
    z.start()
    print(active := active_count())
    print(all := enumerate())
    print(time := perf_counter())
    z.join()
    a.start()

def eat(num):
    sleep(int(num))
    print('eat is done')
    
def coffee(num):
    sleep(int(num))
    print('coffee is done')

def study(num):
    sleep(int(num))
    print('study is done')


def leave(num):
    sleep(int(num))
    print('time to leave')
    
x = Thread(target=eat, args=('3'))
y = Thread(target=coffee, args=('3'))
z = Thread(target=study, args=('4'))
a = Thread(target=leave, args=('2'))

print('\nStarting threads after sleeping\n')
sleeping(3)
