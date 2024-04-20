from typing import List
from project.animals.animal import Bird
from project.food import Food


class Owl(Bird):
    ALLOWED_FOODS: List[Food] = ["Meat"]
    WEIGHT_INCREMENT = 0.25

    def make_sound(self):
        return "Hoot Hoot"
    

class Hen(Bird):
    ALLOWED_FOODS = ['Meat', 'Vegetable', 'Fruit', 'Seed']
    WEIGHT_INCREMENT = 0.35

    def make_sound(self):
        return "Cluck"

