from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30
    VALID_ROBOT = 'MaleRobot'

    def __init__(self, name):
        super().__init__(name, self.CAPACITY)

    def details(self):
        result = f'{self.name} Main Service:\n'
        result += f'Robots: {" ".join([r.name for r in self.robots])}' if self.robots else 'Robots: none'
        return result

