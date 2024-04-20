from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    OXYGEN_LEVEL = 540

    def __init__(self, name: str):
        super().__init__(name, self.OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        penalty = round(0.3 * time_to_catch)
        if penalty >= self.oxygen_level:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= penalty
        # try:
        #     self.oxygen_level -= round(0.3 * time_to_catch)
        # except ValueError:
        #     self.oxygen_level = 0

    def renew_oxy(self):
        self.oxygen_level = 540
