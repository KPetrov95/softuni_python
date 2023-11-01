from _collections import deque

queue_of_people = deque()
amount_of_water = int(input())


while True:
    command = input()
    if command == 'Start':
        break
    else:
        queue_of_people.append(command)

while True:
    command = input()
    if command == 'End':
        print(f"{amount_of_water} liters left")
        break
    elif command.startswith('refill'):
        liters_refill = command.split()[1]
        amount_of_water += int(liters_refill)
    else:
        water_to_drink = int(command)
        person_drinking = queue_of_people.popleft()
        if water_to_drink <= amount_of_water:
            amount_of_water -= water_to_drink
            print(f"{person_drinking} got water" )
        else:
            print(f"{person_drinking} must wait" )