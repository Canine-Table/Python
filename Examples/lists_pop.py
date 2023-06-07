#!/usr/bin/python3

numbers_list = ["One","Two","Three","Four","Five"]
numbers = numbers_list.copy()
numbers.pop(2)
print(numbers)
del numbers[:]
print(numbers)

numbers = numbers_list.copy()
print(numbers.index("One"))

x = [x for x in range(1,11)]
y = [x for x in range(1,11)]

print([(x,y) for x in range(10) for y in range(10) if x != y])

print([abs(x) for x in  [-4,-2,0,2,4]])

matrix = ([1,2,3],[4,5,6],[7,8,9])

print([row[i] for row in matrix for i in range(3)])


print(set("abcdefg"))










