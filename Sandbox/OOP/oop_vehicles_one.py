#!/usr/bin/python3

from datetime import datetime
# import the Vehicle class
from oop_modules.vehicles.car import Car
print(type(datetime.now()))

# create 10 car objects with different attributes
car1 = Car(owner="Alice", brand="Toyota", model="Corolla", color="red", price=20000, year=2020, type="sedan", door_count=4)
car2 = Car(owner="Bob", brand="Tesla", model="Model 3", color="white", price=40000, year=2021, type="sedan", door_count=4, is_electric=True)
car3 = Car(owner="Charlie", brand="Ford", model="F-150", color="black", price=30000, year=2019, type="pickup", door_count=2)
car4 = Car(owner="David", brand="Honda", model="Civic", color="blue", price=25000, year=2020, type="hatchback", door_count=4)
car5 = Car(owner="Eve", brand="BMW", model="X5", color="silver", price=50000, year=2021, type="SUV", door_count=4)
car6 = Car(owner="Frank", brand="Hyundai", model="Elantra", color="green", price=22000, year=2019, type="sedan", door_count=4)
car7 = Car(owner="Grace", brand="Chevrolet", model="Camaro", color="yellow", price=35000, year=2020, type="coupe", door_count=2)
car8 = Car(owner="Harry", brand="Audi", model="Q7", color="brown", price=60000, year=2021, type="SUV", door_count=4)
car9 = Car(owner="Irene", brand="Nissan", model="Leaf", color="purple", price=30000, year=2020, type="hatchback", door_count=4, is_electric=True)
car10 = Car(owner="Jack", brand="Mercedes-Benz", model="C-Class", color="pink", price=45000, year=2021, type="sedan", door_count=4)

# Car object Methods
car1.start().stop().start().stop()
print(car3.__repr__())
print(car6.purchase_date)
print(car9)

for car in Car.all:
    print(car.__repr__())
