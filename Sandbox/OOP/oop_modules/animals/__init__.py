#!/usr/bin/python3

class Animal(object):

    def __init__(self,name: str) -> None:
        self.name: str = name


    def sleep(self) -> object:
        print(f'{self.name} is fast asleep.')
        return self


    def eat(self,food: str) -> object:
        print(f'{self.name} is eating {food}.')
        return self
