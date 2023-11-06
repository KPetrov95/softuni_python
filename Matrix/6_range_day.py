matrix = []
current_position = []
targets_position = []
targets_remaining_count = 0
for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == 'A':
            current_position = [row, col]
        elif matrix[row][col] == 'x':
            targets_position.append([row, col])
            targets_remaining_count += 1

possible_moves = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
targets_hit_count = 0
targets_hit_position = []
number_of_moves = int(input())

for i in range(number_of_moves):
    command = input().split()

    if command[0] == 'move':
        steps = int(command[2])
        new_row = current_position[0] + possible_moves[command[1]][0] * steps
        new_col = current_position[1] + possible_moves[command[1]][1] * steps
        if new_col not in range(5) or new_row not in range(5):
            continue
        elif matrix[new_row][new_col] == 'x':
            continue
        else:
            matrix[current_position[0]][current_position[1]] = '.'
            matrix[new_row][new_col] = 'A'
            current_position = [new_row, new_col]

    elif command[0] == 'shoot':
        r = current_position[0] + possible_moves[command[1]][0]
        c = current_position[1] + possible_moves[command[1]][1]
        while r in range(5) and c in range(5):
            if matrix[r][c] == 'x':
                matrix[r][c] = '.'
                targets_hit_count += 1
                targets_remaining_count -= 1
                targets_hit_position.append([r, c])
                break
            r += possible_moves[command[1]][0]
            c += possible_moves[command[1]][1]
    if targets_remaining_count == 0:
        print(f"Training completed! All {targets_hit_count} targets hit.")
        break
if targets_remaining_count > 0:
    print(f"Training not completed! {targets_remaining_count} targets left.")
for row in targets_hit_position:
    print(row)
