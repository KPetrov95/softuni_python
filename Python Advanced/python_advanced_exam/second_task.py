FISH_NEEDED = 20


def is_valid(target_row, target_column):
    if target_row in range(rows) and target_column in range(rows):
        return True
    return False


rows = int(input())

matrix = []
current_position = []
fish_caught = 0
fell = False

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
    if command == "collect the nets":
        matrix[current_position[0]][current_position[1]] = 'S'
        break
    row_to_go = directions[command][0] + current_position[0]
    col_to_go = directions[command][1] + current_position[1]
    matrix[current_position[0]][current_position[1]] = '-'
    if is_valid(row_to_go, col_to_go):
        current_position = [row_to_go, col_to_go]
        if matrix[row_to_go][col_to_go].isdigit():
            fish_caught += int(matrix[row_to_go][col_to_go])
            matrix[row_to_go][col_to_go] = '-'
        elif matrix[row_to_go][col_to_go] == 'W':
            fell = True
            print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of "
                  f"the ship: [{current_position[0]},{current_position[1]}]")
            break
    else:
        if row_to_go >= rows:
            row_to_go = 0
        elif col_to_go >= rows:
            col_to_go = 0
        current_position = [row_to_go, col_to_go]
        if matrix[row_to_go][col_to_go].isdigit():
            fish_caught += int(matrix[row_to_go][col_to_go])
            matrix[row_to_go][col_to_go] = '-'
        elif matrix[row_to_go][col_to_go] == 'W':
            current_position = [col_to_go, row_to_go]
            fell = True
            print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of "
                  f"the ship: [{current_position[0]},{current_position[1]}]")
            break
    matrix[current_position[0]][current_position[1]] = 'S'
if not fell:
    if fish_caught >= FISH_NEEDED:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {FISH_NEEDED - fish_caught} tons of fish more.")
    if fish_caught > 0:
        print(f"Amount of fish caught: {fish_caught} tons.")
    for row in matrix:
        print(*row, sep='')
