def is_valid(target_row, target_column):
    if target_row in range(rows) and target_column in range(cols):
        if matrix[target_row][target_column] != 'O':
            return True
    return False


rows, cols = [int(x) for x in input().split()]

matrix = []
start_position = []
for i in range(rows):
    matrix.append([x for x in input().split()])
    for j in range(cols):
        if matrix[i][j] == 'B':
            start_position = [i, j]

moves_made = 0
opponents_touched = 0

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

while True:
    command = input()
    if command == 'Finish':
        break
    row_to_go = directions[command][0] + start_position[0]
    col_to_go = directions[command][1] + start_position[1]
    if is_valid(row_to_go, col_to_go):
        if matrix[row_to_go][col_to_go] == 'P':
            opponents_touched += 1
            matrix[row_to_go][col_to_go] = '-'
        moves_made += 1
        start_position = [row_to_go, col_to_go]
    if opponents_touched == 3:
        break
print("Game over!")
print(f"Touched opponents: {opponents_touched} Moves made: {moves_made}")