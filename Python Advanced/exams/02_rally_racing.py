rows = int(input())
car_number = input()
matrix = []
current_position = [0, 0]
tunnels = []
distance = 0
for i in range(rows):
    matrix.append([x for x in input().split()])
    for j in range(rows):
        if matrix[i][j] == 'T':
            tunnels.append((i, j))
directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

while True:
    command = input()
    if command == 'End':
        print(f'Racing car {car_number} DNF.')
        matrix[current_position[0]][current_position[1]] = 'C'
        break
    new_row = directions[command][0] + current_position[0]
    new_col = directions[command][1] + current_position[1]
    matrix[current_position[0]][current_position[1]] = '.'
    if matrix[new_row][new_col] == 'T':
        matrix[new_row][new_col] = '.'
        current_position = [tunnels[1][0], tunnels[1][1]]
        distance += 30
        continue
    elif matrix[new_row][new_col] == 'F':
        distance += 10
        matrix[new_row][new_col] = 'C'
        print(f'Racing car {car_number} finished the stage!')
        break
    matrix[new_row][new_col] = 'C'
    current_position = [new_row, new_col]
    distance += 10
print(f'Distance covered {distance} km.')
for row in matrix:
    print(*row,sep='')