#!/usr/bin/python3

# multiple inheritance
# when a child class is derived from more than onr parent class.


class Organism:

    alive = True

class Animal(Organism):

    def __init__(self,name):
        self.name = name
    def eat(self):
        print(self.name,'is eating.')
 
    def sleep(self):
        print(self.name,'is sleeping.')
        
class Mammal(Animal):
    
    type = 'Mammal'

class Prey:
    def flee(self):
        print(self.name,'is fleeing.')

class Predator:
    def hunt(self):
        print(self.name,'is hunting.')

class Rabbit(Mammal, Prey):
    is_prey = True
    is_predator = False
        

class Dog(Mammal,Predator,Prey):

    is_prey = True
    is_predator = True

    def bark(self):
        print('dog is barking')

dog = Dog('Carl')
print(dog.alive)
print(dog.type)
dog.sleep()
dog.eat()


rabbit = Rabbit('Bill')
dog.hunt()
dog.flee()
print(dog.is_predator,dog.is_prey)
rabbit.flee()
print(rabbit.is_predator,rabbit.is_prey)


