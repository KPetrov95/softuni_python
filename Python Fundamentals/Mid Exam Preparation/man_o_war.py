def fire(warship, fire_index, dmg):
    if fire_index in range(len(warship)):
        warship[fire_index] -= dmg
        if warship[fire_index] <= 0:
            warship = []
            print('You won! The enemy ship has sunken.')
    return warship


def defend(pirate_ship, first_index, second_index, dmg):
    if first_index in range(len(pirate_ship)) and second_index in range(len(pirate_ship)):
        for section in range(first_index, second_index + 1):
            pirate_ship[section] -= dmg
            if pirate_ship[section] <= 0:
                pirate_ship = []
                print("You lost! The pirate ship has sunken.")
                break
    return pirate_ship


def repair(pirate_ship, index, health, max_health):
    if index in range(len(pirate_ship)):
        if pirate_ship[index] + health <= max_health:

            add_health = health
        else:
            add_health = max_health - pirate_ship[index]
        pirate_ship[index] += add_health
    return pirate_ship


def status(pirate_ship, max_health):
    critical_health = 0.2 * max_health
    count = 0
    for section in pirate_ship:
        if section < critical_health:
            count += 1
    return f"{count} sections need repair."


pirate_ship_sections = [int(x) for x in input().split('>')]
navy_ship_sections = [int(x) for x in input().split(">")]
max_health_of_section = int(input())
command = input()
sunken = False

while command != 'Retire':
    command = command.split()
    action = command[0]
    if action == 'Fire':
        index = int(command[1])
        damage = int(command[2])
        navy_ship_sections = fire(navy_ship_sections, index, damage)
    elif action == 'Defend':
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        pirate_ship_sections = defend(pirate_ship_sections, start_index, end_index, damage)
    elif action == 'Repair':
        index = int(command[1])
        healing = int(command[2])
        pirate_ship_sections = repair(pirate_ship_sections, index, healing, max_health_of_section)

    elif action == 'Status':
        print(status(pirate_ship_sections, max_health_of_section))

    if not pirate_ship_sections or not navy_ship_sections:
        sunken = True
        break
    command = input()
if not sunken:
    print(f'Pirate ship status: {sum(pirate_ship_sections)}')
    print(f'Warship status: {sum(navy_ship_sections)}')