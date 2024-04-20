from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    OXYGEN_LEVEL = 120

    def __init__(self, name: str):
        super().__init__(name, self.OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        penalty = round(0.6 * time_to_catch)
        if penalty >= self.oxygen_level:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= penalty

    def renew_oxy(self):
        self.oxygen_level = 120
