#!/usr/bin/python3

from oop_modules.animals import Animal

class Cat(Animal):
    def swat(self,action: str,thing: str) -> object:
        print(f'{self.name} {action} the {thing}.')
        return self
