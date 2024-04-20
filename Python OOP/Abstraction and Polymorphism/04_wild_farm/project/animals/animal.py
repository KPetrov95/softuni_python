from abc import ABC, abstractmethod
from typing import List

from project.food import Food


class Animal(ABC):
    ALLOWED_FOODS: List[Food] = []
    WEIGHT_INCREMENT = 0
    FOOD_EATEN = 0

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food: Food):
        if food.__class__.__name__ in self.ALLOWED_FOODS:
            self.weight += self.WEIGHT_INCREMENT * food.quantity
            self.FOOD_EATEN += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float,):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.FOOD_EATEN}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str,):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.FOOD_EATEN}]"