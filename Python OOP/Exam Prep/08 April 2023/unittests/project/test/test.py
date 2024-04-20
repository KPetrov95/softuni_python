from project.tennis_player import TennisPlayer
from unittest import TestCase, main

class TennisPlayerTests(TestCase):
    def setUp(self):
        self.test_player = TennisPlayer('Grisho', 25, 100.0)

    def test_init_success(self):
        self.assertEqual('Grisho', self.test_player.name)
        self.assertEqual(25, self.test_player.age)
        self.assertEqual(100.0, self.test_player.points)

    def test_setters_equal_to_two(self):
        with self.assertRaises(ValueError) as ve:
            self.test_player.name = 'gr'
        msg = 'Name should be more than 2 symbols!'
        self.assertEqual(msg, str(ve.exception))

    def test_setters_empty_name(self):
        with self.assertRaises(ValueError) as ve:
            self.test_player.name = ''
        msg = 'Name should be more than 2 symbols!'
        self.assertEqual(msg, str(ve.exception))

    def test_age_less_than_18(self):
        with self.assertRaises(ValueError) as ve:
            self.test_player.age = 17
        msg = "Players must be at least 18 years of age!"
        self.assertEqual(msg, str(ve.exception))

    def test_add_new_win_success(self):
        self.test_player.add_new_win('Wimbledon')
        self.assertEqual(['Wimbledon'], self.test_player.wins)

    def test_add_new_win_already_added(self):
        self.test_player.add_new_win('Wimbledon')
        result = self.test_player.add_new_win('Wimbledon')
        msg = f"Wimbledon has been already added to the list of wins!"
        self.assertEqual(msg, result)

    def test_lt_other_better(self):
        other_player = TennisPlayer('Nadal', 30, 500)
        result = self.test_player < other_player
        msg = 'Nadal is a top seeded player and he/she is better than Grisho'
        self.assertEqual(msg, result)

    def test_lt_self_better(self):
        other_player = TennisPlayer('Nadal', 30, 50)
        result = self.test_player < other_player
        msg =f'{self.test_player.name} is a better player than {other_player.name}'
        self.assertEqual(msg, result)

    def test_str_2_wins(self):
        self.test_player.add_new_win('Wimbledon')
        self.test_player.add_new_win('Rolland Garos')
        result = str(self.test_player)
        msg = f"Tennis Player: {self.test_player.name}\n" \
               f"Age: {self.test_player.age}\n" \
               f"Points: {self.test_player.points:.1f}\n" \
               f"Tournaments won: {', '.join(self.test_player.wins)}"
        self.assertEqual(msg, result)

    def test_str_0_wins(self):

        result = str(self.test_player)
        msg = f"Tennis Player: {self.test_player.name}\n" \
               f"Age: {self.test_player.age}\n" \
               f"Points: {self.test_player.points:.1f}\n" \
               f"Tournaments won: {', '.join(self.test_player.wins)}"
        self.assertEqual(msg, result)


if __name__ == '__main__':
    main()
