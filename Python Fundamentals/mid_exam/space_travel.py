list_of_actions = input().split('||')
initial_fuel = int(input())
initial_ammo = int(input())

for action in list_of_actions:
    if action == 'Titan':
        print("You have reached Titan, all passengers are safe.")
        break
    else:
        event, value = action.split()
        value = int(value)
        if event == 'Travel':
            if initial_fuel < value:
                print("Mission failed.")
                break
            initial_fuel -= value
            print(f'The spaceship travelled {value} light-years.')
        elif event == 'Enemy':
            if initial_ammo >= value:
                initial_ammo -= value
                print(f"An enemy with {value} armour is defeated.")
            elif initial_fuel > 2 * value:
                initial_fuel -= 2 * value
                print(f"An enemy with {value} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break
        elif event == 'Repair':
            initial_ammo += 2 * value
            initial_fuel += value
            print(f"Ammunitions added: {2 * value}.")
            print(f"Fuel added: {value}.")
        elif event == 'Titan':
            print("You have reached Titan, all passengers are safe.")
            break
