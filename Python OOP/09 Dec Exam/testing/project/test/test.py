from unittest import TestCase, main
from project.railway_station import RailwayStation
from collections import deque


class RailwayStationTests(TestCase):
    def setUp(self):
        self.test_station = RailwayStation("test")

    def test_init(self):
        self.assertEqual("test", self.test_station.name)

    def test_setter_less_than_three(self):
        error = "Name should be more than 3 symbols!"
        with self.assertRaises(ValueError) as ve:
            self.test_station.name = 'te'
        self.assertEqual(error, str(ve.exception))

    def test_setter_three(self):
        error = "Name should be more than 3 symbols!"
        with self.assertRaises(ValueError) as ve:
            self.test_station.name = 'tes'
        self.assertEqual(error, str(ve.exception))

    def test_new_arrival(self):
        self.assertEqual(deque(), self.test_station.arrival_trains)
        self.test_station.new_arrival_on_board("Varna-Sofia")
        self.assertEqual(deque(['Varna-Sofia']), self.test_station.arrival_trains)

    def test_train_has_arrived_okay(self):
        self.test_station.new_arrival_on_board("Varna-Sofia")
        result = self.test_station.train_has_arrived("Varna-Sofia")
        msg = f"Varna-Sofia is on the platform and will leave in 5 minutes."
        self.assertEqual(msg, result)
        self.assertEqual(deque(['Varna-Sofia']), self.test_station.departure_trains)

    def test_train_has_arrived_another_before(self):
        self.test_station.new_arrival_on_board("Varna-Sofia")
        self.test_station.new_arrival_on_board("Varna-Plovdiv")
        result = self.test_station.train_has_arrived("Varna-Plovdiv")
        msg = "There are other trains to arrive before Varna-Plovdiv."
        self.assertEqual(msg, result)
        self.assertEqual(deque(['Varna-Sofia', 'Varna-Plovdiv']), self.test_station.arrival_trains)

    def test_train_has_left_True(self):
        self.test_station.new_arrival_on_board("Varna-Sofia")
        self.test_station.train_has_arrived("Varna-Sofia")
        self.assertEqual(deque(['Varna-Sofia']), self.test_station.departure_trains)
        self.assertTrue(self.test_station.train_has_left("Varna-Sofia"))
        self.assertEqual(deque(), self.test_station.departure_trains)

    def test_train_has_left_False(self):
        self.test_station.new_arrival_on_board("Varna-Sofia")
        self.test_station.train_has_arrived("Varna-Sofia")
        self.assertEqual(deque(['Varna-Sofia']), self.test_station.departure_trains)
        self.assertFalse(self.test_station.train_has_left("Varna-Plovdiv"))
        self.assertEqual(deque(['Varna-Sofia']), self.test_station.departure_trains)


if __name__ == '__main__':
    main()