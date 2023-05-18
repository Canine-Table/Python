#!/usr/bin/python3

# Daemon Threads
# a thread that runs in the background, not important for program to run
# your program will still not wait for your program to complete before exiting
# non-daemon threads cannot normally be killed, stay alive until task is complete

# ex, background tasks, garbage collection, systemd services, waiting for input,
# long running processes, etc.

from threading import *
from time import *

def timer(num):
    print()
    count = 0
    while True:
        sleep(int(num))
        count += 1
        print('logged in for:',count,'seconds')

x = Thread(target=timer,args=('1'),daemon=True)
x.start()

answer = input('do you wish to quit?: ')
