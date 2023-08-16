#!/usr/bin/python3

from oop_modules.animals import Animal

class Dog(Animal):
    def fetch(self,thing: str) -> object:
        print(f'{self.name} goes after the {thing}.')
        return self
