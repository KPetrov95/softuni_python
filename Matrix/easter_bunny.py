n = int(input())

matrix = []
bunny = []

for i in range(n):
    matrix.append([x for x in input().split()])
    for j in range(n):
        if matrix[i][j] == 'B':
            bunny = [i, j]

possible_moves = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
most_eggs = float('-inf')
best_direction = ''
max_eggs_moves = []
for direction, move in possible_moves.items():
    new_row = bunny[0] + move[0]
    new_col = bunny[1] + move[1]
    current_eggs = 0
    current_moves = []
    while new_row in range(n) and new_col in range(n):
        if matrix[new_row][new_col] == 'X':
            break
        current_eggs += int(matrix[new_row][new_col])
        current_moves.append([new_row, new_col])
        new_row += move[0]
        new_col += move[1]
        if current_eggs > most_eggs:
            most_eggs = current_eggs
            max_eggs_moves = current_moves
            best_direction = direction


print(best_direction)
for row in max_eggs_moves:
    print(row)
print(most_eggs)


