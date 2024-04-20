from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AC_CONSUMPTION = 0.9

    def __init__(self,fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int):
        consumption_for_distance = (self.fuel_consumption + Car.AC_CONSUMPTION) * distance
        if self.fuel_quantity >= consumption_for_distance:
            self.fuel_quantity -= consumption_for_distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_CONSUMPTION = 1.6

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        consumption_for_distance = (self.fuel_consumption + Truck.AC_CONSUMPTION) * distance
        if self.fuel_quantity >= consumption_for_distance:
            self.fuel_quantity -= consumption_for_distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
