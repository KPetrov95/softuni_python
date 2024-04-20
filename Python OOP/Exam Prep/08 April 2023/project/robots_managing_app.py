from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = {'MainService': MainService, 'SecondaryService': SecondaryService}
    VALID_ROBOTS = {'MaleRobot': MaleRobot, 'FemaleRobot': FemaleRobot}
    SERVICE_TYPES = {"MainService": MainService, "SecondaryService": SecondaryService}
    ROBOT_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    ERROR_MSG_TYPE_SERVICE = "Invalid service type!"
    ERROR_MSG_TYPE_ROBOT = "Invalid robot type!"
    ERROR_MSG_CAPACITY = "Not enough capacity for this robot!"
    ERROR_MSG_NO_ROBOT = "No such robot in this service!"

    def __init__(self):
        self.robots: [BaseRobot] = []
        self.services: [BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICES:
            raise Exception("Invalid service type!")
        new_service = self.VALID_SERVICES[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")
        new_robot = self.VALID_ROBOTS[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        current_robot = next((r for r in self.robots if r.name == robot_name), None)
        current_service = next(s for s in self.services if s.name == service_name)
        if current_service.VALID_ROBOT != current_robot.TYPE:
            return "Unsuitable service."
        if len(current_service.robots) >= current_service.capacity:
            raise Exception("Not enough capacity for this robot!")
        self.robots.remove(current_robot)
        current_service.robots.append(current_robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        current_service = next((s for s in self.services if s.name == service_name), None)
        current_robot = next((r for r in current_service.robots if r.name == robot_name), None)
        if current_robot not in current_service.robots:
            raise Exception("No such robot in this service!")
        current_service.robots.remove(current_robot)
        self.robots.append(current_robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service_obj = self._find_obj_by_name(service_name, self.services)
        [r.eating() for r in service_obj.robots]
        return f"Robots fed: {len(service_obj.robots)}."

    def service_price(self, service_name: str):
        current_service = next(s for s in self.services if s.name == service_name)
        total_price = sum([r.price for r in current_service.robots])
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = [s.details() for s in self.services]
        return '\n'.join(result)

    def _check_service_type(self, service_type):
        if service_type not in self.SERVICE_TYPES:
            raise Exception(self.ERROR_MSG_TYPE_SERVICE)

    def _check_robot_type(self, robot_type):
        if robot_type not in self.ROBOT_TYPES:
            raise Exception(self.ERROR_MSG_TYPE_ROBOT)

    def _create_service(self, service_type, name):
        return self.SERVICE_TYPES[service_type](name)

    def _create_robot(self, robot_type, name, kind, price):
        return self.ROBOT_TYPES[robot_type](name, kind, price)

    @staticmethod
    def _find_obj_by_name(name, collection):  # existing name
        return [obj for obj in collection if obj.name == name][0]
