from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTests(TestCase):
    def setUp(self):
        self.test_vehicle = Vehicle(10.0, 100.0)

    def test_init_vehicle(self):
        self.assertEqual(10.0, self.test_vehicle.fuel)
        self.assertEqual(10.0, self.test_vehicle.capacity)
        self.assertEqual(100.0, self.test_vehicle.horse_power)
        self.assertEqual(1.25, self.test_vehicle.fuel_consumption)

    def test_drive_success(self):
        self.test_vehicle.drive(5)
        self.assertEqual(3.75, self.test_vehicle.fuel)

    def test_drive_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.drive(10)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_success(self):
        self.test_vehicle.drive(5)
        self.test_vehicle.refuel(5)
        self.assertEqual(8.75, self.test_vehicle.fuel)

    def test_refuel_too_much_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.refuel(5)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str(self):
        expected = f"The vehicle has 100.0 " \
               f"horse power with 10.0 fuel left and 1.25 fuel consumption"
        actual = str(self.test_vehicle)
        self.assertEqual(expected, actual)
if __name__ == '__main__':
    main()
