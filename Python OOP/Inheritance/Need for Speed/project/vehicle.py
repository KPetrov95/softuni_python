class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        self.horse_power = horse_power

    def drive(self, kilometers):
        if self.fuel_consumption * kilometers <= self.fuel:
            self.fuel -= self.fuel_consumption * kilometers
        