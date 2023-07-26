def heroes_assemble(hero_data, dict_of_heroes):
    hero_name, health, mana = hero_data.split()
    dict_of_heroes[hero_name] = {'HP': int(health), 'MP': int(mana)}
    return dict_of_heroes


def cast_spell(list_of_heroes, list_values):
    hero_name, mana, spell_name = list_values
    if hero_name in list_of_heroes.keys():
        if list_of_heroes[hero_name]['MP'] >= int(mana):
            list_of_heroes[hero_name]['MP'] -= int(mana)
            print(f"{hero_name} has successfully cast {spell_name} and now has {list_of_heroes[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    return list_of_heroes


def take_damage(list_of_heroes, list_values):
    hero_name, damage, attacker = list_values
    if hero_name in list_of_heroes.keys():
        list_of_heroes[hero_name]['HP'] -= int(damage)
        if list_of_heroes[hero_name]['HP'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {list_of_heroes[hero_name]['HP']}"
                  f" HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del list_of_heroes[hero_name]
    return list_of_heroes


def recharge(list_of_heroes, list_values):

    hero_name, amount = list_values
    amount = int(amount)
    if hero_name in list_of_heroes.keys():
        if list_of_heroes[hero_name]['MP'] + amount > 200:
            amount = 200 - list_of_heroes[hero_name]['MP']
        list_of_heroes[hero_name]['MP'] += amount
        print(f"{hero_name} recharged for {amount} MP!")
    return list_of_heroes


def heal(list_of_heroes, list_values):
    hero_name, amount = list_values
    amount = int(amount)
    if hero_name in list_of_heroes.keys():
        if list_of_heroes[hero_name]['HP'] + amount > 100:
            amount = 100 - list_of_heroes[hero_name]['HP']
        list_of_heroes[hero_name]['HP'] += amount
        print(f"{hero_name} healed for {amount} HP!")
    return list_of_heroes


number = int(input())
all_heroes = {}


for current_hero_number in range(number):
    data = input()
    heroes_assemble(data, all_heroes)

while True:
    command, *values = input().split(' - ')
    if command == 'End':
        for hero, stats in all_heroes.items():
            print(f'{hero}')
            print(f"  HP: {stats['HP']}")
            print(f"  MP: {stats['MP']}")
        break
    elif command == 'CastSpell':
        all_heroes = cast_spell(all_heroes, values)
    elif command == 'TakeDamage':
        all_heroes = take_damage(all_heroes, values)
    elif command == 'Recharge':
        all_heroes = recharge(all_heroes, values)
    elif command == 'Heal':
        all_heroes = heal(all_heroes, values)
