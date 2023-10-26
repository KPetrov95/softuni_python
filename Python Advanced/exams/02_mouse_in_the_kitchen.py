rows, cols = [int(x) for x in input().split(',')]
matrix = []
start_position = []
total_cheeses = 0
for i in range(rows):
    matrix.append([x for x in input()])
    for j in range(cols):
        if matrix[i][j] == 'M':
            start_position = [i, j]
        elif matrix[i][j] == 'C':
            total_cheeses += 1
directions = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}

while True:
    command = input()
    if command == 'danger':
        print("Mouse will come back later!")
        break
    new_row = directions[command][0] + start_position[0]
    new_col = directions[command][1] + start_position[1]
    if new_row not in range(rows) or new_col not in range(cols):
        print("No more cheese for tonight!")
        break
    elif matrix[new_row][new_col] == '@':
        continue
    matrix[start_position[0]][start_position[1]] = "*"
    start_position = [new_row, new_col]
    if matrix[new_row][new_col] == 'C':
        total_cheeses -= 1
        matrix[new_row][new_col] = 'M'

        if total_cheeses <= 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif matrix[new_row][new_col] == 'T':
        matrix[new_row][new_col] = 'M'
        start_position = [new_row, new_col]
        print("Mouse is trapped!")
        break
    matrix[new_row][new_col] = 'M'

for row in matrix:
    print(*row, sep="")