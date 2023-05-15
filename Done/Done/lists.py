#!/usr/bin/python3

# lists
# used to store muliple items in a single variable

my_list = ["one","two","three","four","five"]

print(my_list)

for i in range(my_list.__len__()):
    print(str(i)+": "+str(my_list[i]))
my_list.append("six")
my_list.insert(0,"zero")
my_list.pop()
my_list.sort()
for j in my_list:
    print(j)
my_list.clear()
print(my_list)