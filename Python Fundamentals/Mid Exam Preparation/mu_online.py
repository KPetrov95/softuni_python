rooms_list = input().split('|')
health = 100
bitcoins = 0
rooms = 0
for room in rooms_list:
    event, value = room.split()
    rooms += 1
    value = int(value)
    if event == 'potion':
        if health + value >= 100:
            value = 100 - health
        health += value
        print(f"You healed for {value} hp.\nCurrent health: {health} hp.")
    elif event == 'chest':
        print(f'You found {value} bitcoins.')
        bitcoins += value
    else:
        monster = event
        health -= value
        if health <= 0:
            print(f'You died! Killed by {monster}.')
            print(f"Best room: {rooms}")
            break
        else:
            print(f"You slayed {monster}.")
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")


