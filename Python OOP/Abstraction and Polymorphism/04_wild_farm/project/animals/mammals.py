from project.animals.animal import Mammal


class Mouse(Mammal):
    ALLOWED_FOODS = ['Vegetable', 'Fruit']
    WEIGHT_INCREMENT = 0.1

    def make_sound(self):
        return "Squeak"


class Cat(Mammal):
    ALLOWED_FOODS = ['Meat', 'Vegetable']
    WEIGHT_INCREMENT = 0.30

    def make_sound(self):
        return "Meow"


class Dog(Mammal):
    ALLOWED_FOODS = ['Meat']
    WEIGHT_INCREMENT = 0.40

    def make_sound(self):
        return "Woof!"

class Tiger(Mammal):
    ALLOWED_FOODS = ['Meat']
    WEIGHT_INCREMENT = 1

    def make_sound(self):
        return "ROAR!!!"