list_of_events = input().split("|")

total_coins = 100
total_energy = 100
shop_closed = False

for event in list_of_events:
    event_type, event_value = event.split('-')
    event_value = int(event_value)
    if event_type == 'rest':
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f'You gained {gained_energy} energy.')
        print(f"Current energy: {total_energy}.")
    elif event_type == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_value
            print(f'You earned {event_value} coins.')
        else:
            total_energy += 50
            print('You had to rest!')
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {event_type}.")
        else:
            shop_closed = True
        if shop_closed:
            print(f"Closed! Cannot afford {event_type}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")

