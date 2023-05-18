#!/usr/bin/python3

# ******************************************

#   Python Multiprocessing

# ******************************************

# Multiprocessing
# running tasks in parrallel on different cpu, cores, 
# bypasses the GIL used for threads

# mutliprocessing
# better for cpu bound tasks (heavy cpu usage)

# multithreading
# better for I/O bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counting(num):
    z = Process(target=is_still_alice)
    z.start()
    count = 0
    while count < num:
        count += 1
    z.kill()

def is_still_alice():
    time_to_finished = 0
    while True:
        time.sleep(1)
        time_to_finished += 1
        print(time_to_finished)

def main():
    print('cpu count:',cpu_count())
    a = Process(target=counting,args=(250000000,))
    b = Process(target=counting,args=(250000000,))
    c = Process(target=counting,args=(250000000,))
    d = Process(target=counting,args=(250000000,))
    a.start()
    b.start()
    c.start()
    d.start()
    
    a.join()
    b.join()
    c.join()
    d.join()

if __name__ == '__main__':
    main()
