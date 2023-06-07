#!/usr/bin/python3

from modules.my_modules import *

# list.append("value/iterable") == list.insert(len(list),"value/iterable")
# list.clear() == del list[:]
# list.extend(iterable) == list[len(list):] = iterable
# list.append("value") == list[len(list):] = "value/iterable"
# list.copy == list[:]

# list.insert(0,"value")
# list.index("value"[,start[,stop]])
# list.sort(key=None,reverse=False)


my_animal_lists = [
    ["oryx","bat","mouse","panda","dormouse","woodchuck","octopus","pig","jackal","opossum"],
    ["dung beetle","guanaco","parakeet","coati","wolf","prairie dog","starfish","lynx","musk deer","lion"],
    ["bull","budgerigar","gnu","koala","jaguar","eland","squirrel","waterbuck","lovebird","mink"]
]

my_animal_list = []

for i in my_animal_lists:
    my_animal_list[len(my_animal_list):] = [i]

print(hr,my_animal_list,hr)

del my_animal_list[:]

for i in my_animal_lists:
    my_animal_list.extend(i)

print(my_animal_list,hr)

my_animals_joined = " ".join(my_animal_list)
print(my_animals_joined,hr)

my_animals_split = my_animals_joined.split(" ")
print(my_animals_split,hr)

print("number of spaces:",my_animals_joined.count(" "),hr)

print("sort the list:",sorted(my_animals_split),hr)
print("sort the list reversed:",list(reversed(sorted(my_animal_list))),hr)

print("sort the list reverse the words:","".join(list(reversed(my_animals_joined))).split(" "),hr)

print(dict(enumerate(my_animal_list)))


my_animal_list.clear()
