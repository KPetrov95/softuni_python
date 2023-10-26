size = int(input())
matrix = []
squirrel_position = []
hazelnuts = 0
moves = [x for x in input().split(', ')]
for row in range(size):
    matrix.append([x for x in input()])
    for col in range(size):
        if matrix[row][col] == 's':
            squirrel_position = [row, col]

directions = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}

for current_move in moves:
    next_row = squirrel_position[0] + directions[current_move][0]
    next_col = squirrel_position[1] + directions[current_move][1]
    if next_row not in range(size) or next_col not in range(size):
        print("The squirrel is out of the field.")
        break
    if matrix[next_row][next_col] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        break
    if matrix[next_row][next_col] == 'h':
        hazelnuts += 1
        matrix[next_row][next_col] = '*'
    if hazelnuts >= 3:
        print("Good job! You have collected all hazelnuts!")
        break
    squirrel_position = [next_row, next_col]
else:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {hazelnuts}")
