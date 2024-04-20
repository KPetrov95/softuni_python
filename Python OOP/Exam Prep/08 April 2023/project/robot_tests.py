from project.robots_managing_app import RobotsManagingApp
from unittest import TestCase, main
from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService

class RobottestsApp(TestCase):
    def setUp(self) -> None:
        self.main_app = RobotsManagingApp()

    def test_add_robot(self):
        self.main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.0)
        self.assertEqual(1, len(self.main_app.robots))
        with self.assertRaises(Exception) as ex:
            self.main_app.add_robot('FemaleRobots', 'Scrap', 'HouseholdRobots', 321.0)
        self.assertEqual("Invalid robot type!", str(ex.exception))
if __name__ == '__main__':
    main()