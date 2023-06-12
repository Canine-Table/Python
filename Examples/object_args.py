#!/usr/bin/python3

class Vehicle:
    color = None

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

def change_color(vehicle,color):
    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()
motorcycle_1 = Motorcycle()
motorcycle_2 = Motorcycle()
motorcycle_3 = Motorcycle()

change_color(car_1,'gold')
change_color(car_2,'green')
change_color(car_3,'blue')
change_color(motorcycle_1,'gray')
change_color(motorcycle_2,'yellow')
change_color(motorcycle_3,'red')

print('{}\n{}\n{}\n{}\n{}\n{}\n'.format(car_1.color,car_2.color,car_3.color,motorcycle_1.color,motorcycle_2.color,motorcycle_3.color))
