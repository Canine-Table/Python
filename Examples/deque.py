#!/usr/bin/python3

from collections import deque

queue = deque(["Eric","John","Michael"])

queue.append("Terry")
queue.append("Graham")
queue.popleft()

queue_items = [queue[x] for x in range(0,queue.__len__())]

print(queue_items)
