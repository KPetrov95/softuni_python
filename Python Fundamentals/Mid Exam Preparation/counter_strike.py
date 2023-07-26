total_energy = int(input())
command = input()
games_won = 0

while command != 'End of battle':
    distance = int(command)

    if total_energy >= distance and total_energy > 0:
        total_energy -= distance
        games_won += 1
        if games_won % 3 == 0:
            total_energy += games_won
    else:
        print(f'Not enough energy! Game ends with {games_won} won battles and {total_energy} energy')
        break
    command = input()
else:
    print(f'Won battles: {games_won}. Energy left: {total_energy}')