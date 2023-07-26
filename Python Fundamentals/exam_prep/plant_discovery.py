def rate(plants, target_plant, value):
    if target_plant in plants:
        plants[target_plant][1].append(value)
    else:
        print("error")
    return plants


def update(plants, target_plant, value):
    if target_plant in plants:
        plants[target_plant][0] = value
    else:
        print("error")
    return plants


def reset(plants, target_plant):
    if target_plant in plants:
        plants[target_plant][1] = []
    else:
        print("error")
    return plants


number_of_plants = int(input())
all_plants = {}

for plants in range(number_of_plants):
    plant_name, rarity = input().split('<->')
    rating = []
    all_plants[plant_name] =[rarity, rating]

while True:
    command = input().split(': ')
    if command[0] == 'Exhibition':
        break
    plant_data = command[1]
    if command[0] == 'Reset':
        all_plants = reset(all_plants, plant_data)
    elif command[0] == 'Rate':
        plant_name, rating = plant_data.split(' - ')
        rating = int(rating)
        all_plants = rate(all_plants, plant_name, rating)
    elif command[0] == 'Update':
        plant_name, new_rarity = plant_data.split(' - ')
        new_rarity = int(new_rarity)
        all_plants = update(all_plants, plant_name, new_rarity)
print('Plants for the exhibition:')
for key, value in all_plants.items():
    rarity = value[0]
    if value[1]:
        average_rating = sum(value[1]) / len(value[1])
    else:
        average_rating = 0
    print(f'- {key}; Rarity: {rarity}; Rating: {average_rating:.2f}')