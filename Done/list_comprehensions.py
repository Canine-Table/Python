#!/usr/bin/python3

# list comprehentions
# a way to create a new list with less syntax
# can mimic certain lambda functions. easier to read
#   list = [expression for item in iterable]
#   list = [expression for item in iterable if conditional]
#   list = [expression if/else for item in iterable]

squares = []
for i in range(1,11):
    squares.append(i * i)
    print(i)
print(squares)


for j in [i * i * i for i in range(1,11)]:
    print(j)

grades = [i * 7 for i in range(1,11)]

print(list(filter(lambda x: x >= 50, grades)))

for j in list(filter(lambda x: x >= 50, grades)):
    print('passed:', j)

for j in list(filter(lambda x: x < 50, grades)):
    print('failed:',j)
    
my_list = []
print('\n\nmarks\n-----\n')
for j in [i if (i * 7) < 50 else print('Passed:',i * 7) for i in range(1,11)]:
    if j != None:
        print('Failed:',j * 7)
        my_list += str(j)

print('\n\nfailed\n------\n')
for i in my_list:
    print('Failed:',int(i)*7)
