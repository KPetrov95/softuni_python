from project.second_hand_car import SecondHandCar
from unittest import TestCase, main

class SecondHandCarTests(TestCase):
    def setUp(self):
        self.test_car = SecondHandCar('alfa159', 'estate', 500, 1000.0)

    def test_init_all_ok(self):
        self.assertEqual('alfa159', self.test_car.model)
        self.assertEqual('estate', self.test_car.car_type)
        self.assertEqual(500, self.test_car.mileage)
        self.assertEqual(1000, self.test_car.price)
        self.assertEqual([], self.test_car.repairs)

    def test_init_price_setter_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test_car.price = 0.9
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_init_mileage_setter_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test_car.mileage = 50
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promotional_price_success(self):
        result = self.test_car.set_promotional_price(800)
        self.assertEqual('The promotional price has been successfully set.', result)

    def test_set_promotional_price_equal_price(self):
        msg = 'You are supposed to decrease the price!'
        with self.assertRaises(ValueError) as ve:
            self.test_car.set_promotional_price(1000)
        self.assertEqual(msg, str(ve.exception))

    def test_set_promotional_price_higher_price(self):
        msg = 'You are supposed to decrease the price!'
        with self.assertRaises(ValueError) as ve:
            self.test_car.set_promotional_price(1100)
        self.assertEqual(msg, str(ve.exception))

    def test_need_repair_success(self):
        result = self.test_car.need_repair(100, 'change oil')
        self.assertEqual(1100, self.test_car.price)
        self.assertEqual(['change oil'], self.test_car.repairs)
        self.assertEqual('Price has been increased due to repair charges.', result)

    def test_need_repair_expensive(self):
        result = self.test_car.need_repair(1000, 'ala-bala')
        self.assertEqual('Repair is impossible!', result)
        self.assertEqual(1000, self.test_car.price)
        self.assertEqual([], self.test_car.repairs)

    def test_gt_type_mismatch(self):
        self.test_other_car = SecondHandCar('alfa159', 'saloon', 500, 1000.0)
        result = self.test_car.__gt__(self.test_other_car)
        msg = 'Cars cannot be compared. Type mismatch!'
        self.assertEqual(msg, result)

    def test_gt_other_cheaper(self):
        self.test_other_car = SecondHandCar('alfa159', 'estate', 500, 900.0)
        result = self.test_car.__gt__(self.test_other_car)
        self.assertTrue(result)

    def test_gt_other_same_price(self):
        self.test_other_car = SecondHandCar('alfa159', 'estate', 500, 1000.0)
        result = self.test_car.__gt__(self.test_other_car)
        self.assertFalse(result)

    def test_gt_other_more_expensive(self):
        self.test_other_car = SecondHandCar('alfa159', 'estate', 500, 1100.0)
        result = self.test_car.__gt__(self.test_other_car)
        self.assertFalse(result)

    def test_str(self):
        msg = f"""Model {self.test_car.model} | Type {self.test_car.car_type} | Milage {self.test_car.mileage}km
Current price: {self.test_car.price:.2f} | Number of Repairs: {len(self.test_car.repairs)}"""
        result = str(self.test_car)
        self.assertEqual(msg, result)



if __name__ == '__main__':
    main()
