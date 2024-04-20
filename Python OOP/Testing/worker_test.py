from unittest import TestCase, main
#from CarManager.car_manager import Car

class TestCarManager(TestCase):
    def setUp(self):
        self.car = Car("Alfa", "159", 1, 10)

    def test_correct_init(self):
        self.assertEqual("Alfa", self.car.make)
        self.assertEqual("159", self.car.model)
        self.assertEqual(1, self.car.fuel_consumption)
        self.assertEqual(10, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_null_value(self):
        with self.assertRaises(Exception) as ex:
            car = Car("", "159", 1, 10)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_null_value(self):
        with self.assertRaises(Exception) as ex:
            car = Car("alfa", "", 1, 10)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_zero(self):
        with self.assertRaises(Exception) as ex:
            car = Car("alfa", "159", 0, 10)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_zero(self):
        with self.assertRaises(Exception) as ex:
            car = Car("alfa", "159", 10, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_zero(self):
        with self.assertRaises(Exception) as ex:
            car = Car("alfa", "159", 10, 10)
            car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_normal(self):
        self.car.refuel(8)
        self.assertEqual(8, self.car.fuel_amount)

    def test_refuel_more_than_capacity_fills_to_capacity(self):
        self.car.refuel(11)
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_negative_amount_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive_successful(self):
        self.car.refuel(10)
        self.car.drive(100)
        self.assertEqual(9, self.car.fuel_amount)

    def test_drive_not_enough_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

if __name__ == "__main__":
    main()