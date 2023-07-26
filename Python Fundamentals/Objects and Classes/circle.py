class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.area = diameter / 2

    def calculate_circumference(self):
        return 2 * Circle.__pi * self.area

    def calculate_area(self):
        return Circle.__pi * self.area ** 2

    def calculate_area_of_sector(self, angle):

        return 0.5 * self.area ** 2 * (angle / 57.3)


circle = Circle(10)
angle = 5
print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")