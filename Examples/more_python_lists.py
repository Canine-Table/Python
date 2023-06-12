#!/usr/bin/python3

from modules.my_modules import *

animals_list = my_animal_lists.copy()
animals_list.append(appended_animals := ["beaver","jackal","lamb","chinchilla","zebu","buffalo","dog","cheetah","alligato","mandrill"],)

def animal_comprehention(get_list):
    return [my_list[i] for my_list in get_list for i in range(0,len(my_list))]

def get_animal_list(copy_list,append_list):
    new_list = copy_list.copy()
    new_list.append(append_list)
    return new_list

def return_dictionary(get_list):
    values = [my_list[k] for my_list in get_list for k in range(0,len(my_list))]
    return dict(enumerate(values))

animals = animal_comprehention(animals_list)
print(hr,set(animals),hr)
print(animals_list.pop(3),hr)
print(animals_list.pop(0),hr)
print(animals_list.pop(1),hr)
print(animals_list.pop(),hr)

print(animals_list := get_animal_list(my_animal_lists,appended_animals),hr)
print("beaver count: ",animals.count("beaver"),hr)
print(return_dictionary(animals_list))
