#!/usr/bin/python3
import random

def random_int(x,y):
    print(random.randint(x,y))
random_int(1,10)
random_int(1,100)
random_int(1,1000)

def my_list():
    list = ['Rock','Paper','Scissors']
    print(random.choice(list))
my_list()
my_list()
my_list()

cards = ['A',1,2,3,4,5,6,7,8,9,'J','Q','K']
def my_cards(shuffle_array):
    random.shuffle(shuffle_array)
    print(shuffle_array)
my_cards(cards)
my_cards(cards)
my_cards(cards)