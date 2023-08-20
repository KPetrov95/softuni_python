def add(dict_zoo, dict_animals, values):
    animal, needed_food, area = values.split('-')
    if area not in dict_zoo:
        if animal not in dict_zoo.values():
            dict_zoo[area] = [animal]
    else:
        dict_zoo[area].append(animal)
    if animal not in dict_animals:
        dict_animals[animal] = int(needed_food)
    else:
        dict_animals[animal] += int(needed_food)
    return dict_zoo, dict_animals

def feed(dict_zoo, dict_animals, values):
    animal, food = values.split('-')
    if animal in dict_animals:
        dict_animals[animal] -= int(food)
        if dict_animals[animal] <= 0:
            print(f'{animal} was successfully fed')
            del dict_animals[animal]
            for item in dict_zoo.values():
                if animal in item:
                    item.remove(animal)
    return dict_zoo, dict_animals

areas = {}
animals = {}

while True:
    command = input().split(': ')
    if command[0] == 'EndDay':
        break
    data = command[1]
    if command[0] == 'Add':
        areas, animals = add(areas,animals, data)
    elif command[0] == 'Feed':
        areas, animals = feed(areas, animals, data)

print("Animals:")
for key,value in animals.items():
    print(f" {key} -> {value}g")
print("Areas with hungry animals:")
for key,value in areas.items():
    if len(value) > 0:
        print(f"{key}: {len(set(value))}")