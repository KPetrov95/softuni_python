from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15
    VALID_ROBOT = 'FemaleRobot'

    def __init__(self, name):
        super().__init__(name, self.CAPACITY)

    def details(self):
        result = f'{self.name} Secondary Service:\n'
        result += f'Robots: {" ".join([r.name for r in self.robots])}' if self.robots else 'Robots: none'
        return result
