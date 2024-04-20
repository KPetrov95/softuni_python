from unittest import TestCase, main
from project.hero import Hero


class HeroTests(TestCase):
    def setUp(self) -> None:
        self.test_hero = Hero("Boyko", level=10, health=1000.0, damage=100.0)

    def test_init(self):
        self.assertEqual("Boyko", self.test_hero.username)
        self.assertEqual(10, self.test_hero.level)
        self.assertEqual(1000, self.test_hero.health)
        self.assertEqual(100, self.test_hero.damage)

    def test_battle_success_win(self):
        self.enemy_hero = Hero("Delyan", 9, 900, 100)
        result = self.test_hero.battle(self.enemy_hero)
        self.assertEqual(11, self.test_hero.level)
        self.assertEqual(105, self.test_hero.health)
        self.assertEqual(105, self.test_hero.damage)
        self.assertEqual("You win", result)

    def test_battle_success_lose(self):
        self.enemy_hero = Hero("Delyan", 15, 1100, 100)
        result = self.test_hero.battle(self.enemy_hero)
        self.assertEqual(105, self.enemy_hero.health)
        self.assertEqual(16, self.enemy_hero.level)
        self.assertEqual(105, self.enemy_hero.damage)
        self.assertEqual("You lose", result)

    def test_battle_success_draw(self):
        self.enemy_hero = Hero("Delyan", 10, 1000, 100)
        result = self.test_hero.battle(self.enemy_hero)
        self.assertEqual("Draw", result)

    def test_battle_failure_cannot_fight_self(self):
        self.enemy_hero = Hero("Boyko", 10, 1000, 100)
        with self.assertRaises(Exception) as ex:
            self.test_hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_failure_self_hero_health_zero(self):
        self.enemy_hero = Hero("Boyko2", 10, 1000, 100)
        self.test_hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.test_hero.battle(self.enemy_hero)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_battle_failure_enemy_hero_health_zero(self):
        self.enemy_hero = Hero("Boyko2", 10, 0, 100)
        with self.assertRaises(ValueError) as ex:
            self.test_hero.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(ex.exception))

    def test_str(self):
        result = f"Hero {self.test_hero.username}: {self.test_hero.level} lvl\n" \
               f"Health: {self.test_hero.health}\n" \
               f"Damage: {self.test_hero.damage}\n"
        self.assertEqual(result, str(self.test_hero))

if __name__ == '__main__':
    main()