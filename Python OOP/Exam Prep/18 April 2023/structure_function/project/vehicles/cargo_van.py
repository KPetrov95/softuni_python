from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    TYPE = 'CargoVan'
    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=180)

    def drive(self, mileage: float):
        percentage = round(mileage / self.max_mileage * 100)
        percentage += 5
        self.battery_level -= percentage
