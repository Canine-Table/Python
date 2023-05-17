#!/usr/bin/python3

# abstract classes
# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class
# a class which contains one or more abstract methods.

# abstract methods
# a method that has a declaration but does not have an implementation.

from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    
    is_drivable = True

    @abstractclassmethod
    def go(self):
        pass

    @abstractclassmethod
    def park(self):
        pass

    @abstractclassmethod
    def start(self):
        pass

    @abstractclassmethod
    def brake(self):
        pass

class Motorcycle(Vehicle):

    def go(self):
        print('this motorcycle is driving')
        return self

    def start(self):
        print('this motorcycle has started')
        return self

    def brake(self):
        print('this motorcycle has stopped.')
        return self

    def park(self):
        print('this motorcycle has parked.')
        return self

class Car(Vehicle):
    def go(self):
        print('this car is driving')
        return self

    def start(self):
        print('this car has started')
        return self

    def brake(self):
        print('this car has stopped.')
        return self

    def park(self):
        print('this car has parked.')
        return self

car = Car()
car.brake().park()

motorcycle = Motorcycle()
motorcycle.start().go()
