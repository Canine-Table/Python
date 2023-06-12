#!/usr/bin/python3

# Duck Typing
# concept where the class of an object is less important than the methods
# class type is not checked if minimum methods/attributes are present
# "if it walks like a duck, and it quacks like a duck then it must be a duck."

class Bird:
    name = None
    def __init__(self,name):
        self.name = name

class Duck(Bird):

    def walk(self):
        print("This is a walking Duck!")
        return self

    def talk(self):
        print("This is a talking Duck!")
        return self

class Chicken(Bird):

    def walk(self):
        print("This is a walking Chicken!")
        return self
    
    def talk(self):
        print("This is a talking Clucking!")
        return self

class Person:
    def catch(self,duck):
        duck.walk().talk()
        print('you caught yourself a {}!'.format(duck.name))
        return self
    
duck = Duck('duck')
chicken =  Chicken('chicken')
person = Person()

person.catch(chicken)
person.catch(duck)