class Vehicle:

    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def honk(self):
        return "HOOOONK"
    
    def drive(self, miles_driven):
        self.mileage += miles_driven
        return self.mileage
    
    def __repr__(self):
        return f"A {self.year} {self.color} {self.make} {self.model} with {self.mileage} miles";
        

if __name__ == '__main__':
    my_vehicle = Vehicle('toyota', 'camry', 'gray', 2015, 20034)
    print(my_vehicle.mileage)
    print(my_vehicle.honk())
    print(my_vehicle.drive(100))
    print(my_vehicle);
