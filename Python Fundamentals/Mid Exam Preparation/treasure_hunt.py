def loot(chest, list_of_items):
    for item in list_of_items:
        if item not in chest:
            chest.insert(0, item)
    return chest


def drop(chest, item_index):
    if item_index in range(len(chest)):
        dropped_item = chest.pop(item_index)
        chest.append(dropped_item)
    return chest


def steal(chest, count_items):
    if count_items >= len(chest):
        print(", ".join(chest))
        chest = []
    else:
        steal_index = len(chest) - count_items
        print(', '.join(chest[steal_index:]))
        chest = chest[0:steal_index]
    return chest


treasure_chest = input().split('|')
command = input()

while command != "Yohoho!":
    command = command.split()
    action = command[0]
    if action == 'Loot':
        loots = command[1:]
        treasure_chest = loot(treasure_chest, loots)
    elif action == 'Drop':
        index = int(command[1])
        treasure_chest = drop(treasure_chest, index)

    elif action == 'Steal':
        count = int(command[1])
        treasure_chest = steal(treasure_chest, count)
    command = input()

if not treasure_chest:
    print("Failed treasure hunt.")
else:
    average = sum(len(item) for item in treasure_chest) / len(treasure_chest)
    print(f"Average treasure gain: {average:.2f} pirate credits.")