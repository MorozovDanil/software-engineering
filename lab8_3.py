class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

class ElectricCar(Car):
    def __init__(self,make,model,battery_capacity):
        super().__init__(make,model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

my_ElectricCar = ElectricCar("Tesla","Model S",75)
my_ElectricCar.charge()
my_ElectricCar.drive()