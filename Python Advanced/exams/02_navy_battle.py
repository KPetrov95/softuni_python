rows = int(input())

matrix = []
current_position = []
mine_hits = 0
ships_hits = 0
for i in range(rows):
    matrix.append([x for x in input()])
    for j in range(rows):
        if matrix[i][j] == 'S':
            current_position = [i, j]

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

while True:
    command = input()
    new_row = directions[command][0] + current_position[0]
    new_col = directions[command][1] + current_position[1]
    matrix[current_position[0]][current_position[1]] = '-'
    current_position = [new_row, new_col]
    if matrix[new_row][new_col] == '*':
        mine_hits += 1
        matrix[new_row][new_col] = '-'
        if mine_hits == 3:
            matrix[new_row][new_col] = 'S'
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{new_row}, {new_col}]!")
            break
    elif matrix[new_row][new_col] == 'C':
        ships_hits += 1
        matrix[new_row][new_col] = '-'
        if ships_hits == 3:
            matrix[new_row][new_col] = 'S'
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break
for row in matrix:
    print(*row,sep='')