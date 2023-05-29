#!/usr/bin/python3

class Vehicle:

    def __init__(self,make,model,year,color):
        self.make = make
        self.year = year
        self.color = color
        self.model = model

    def drive(self):
        print('The',self.model,self.make,'started driving')
    
    def get_make(self):
        print('Make:',self.make)

    def get_model(self):
        print('Model:',self.model)

    def get_year(self):
        print('Year:',self.year)
    
    def get_color(self):
        print('Color:',self.color)

    def get_all(self):
        print('Make:',self.make)
        print('Model:',self.model)
        print('Year:',self.year)
        print('Color:',self.color)

class Car(Vehicle):
      
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year, color)
        self.type = 'Car'
    
    def get_all(self):
        print('Type:',self.type)
        return super().get_all()

    def get_type(self):
        print('Type:',self.type)

car_1 = Car('Corolla','Toyota','2002','Red')
car_2 = Car('Camry','Toyota','2023','Green')
car_3 = Car('RAV4','Toyota','2020','Blue')

car_3.drive()
print(car_3.type)
car_3.get_all()