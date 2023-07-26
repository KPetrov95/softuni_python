class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.birds = []
        self.fishes = []

    def add_animal(self, species, animal):
        if species == "mammal":
            self.mammals.append(animal)
        elif species == 'bird':
            self.birds.append(animal)
        elif species == 'fish':
            self.fishes.append(animal)
        Zoo.__animals += 1

    def get_info(self,species):
        if species == "mammal":
            return f"Mammals in {zoo_name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == 'bird':
            return f"Birds in {zoo_name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"
        elif species == 'fish':
            return f"Fishes in {zoo_name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
number_of_animals = int(input())
zoo = Zoo(zoo_name)
Zoo.__animals = number_of_animals

for current_animal in range(number_of_animals):
    species, animal = input().split()

    zoo.add_animal(species, animal)

target_species = input()

print(zoo.get_info(target_species))

