#!/usr/bin/python3

# Method Chaining
# calling multiple methods sequentially
# each call performs an action on the same object and return self

class Car:
    def turn_on(self):
        print('the car is turned on.')
        return self
    def turn_off(self):
        print('the car is turned off')
        return self
    def brake(self):
        print('the car is stopped')
        return self
    def drive(self):
        print('the car is driving')
        return self

car = Car()
car.turn_on().drive().brake().turn_off()