rows, cols = [int(x) for x in input().split()]

matrix = []
start_position = []
for i in range(rows):
    matrix.append([x for x in input()])
    for j in range(cols):
        if matrix[i][j] == 'B':
            start_position = [i, j]

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}
current_position = start_position

while True:
    command = input()
    new_row = directions[command][0] + current_position[0]
    new_col = directions[command][1] + current_position[1]
    if new_row not in range(rows) or new_col not in range(cols):
        matrix[start_position[0]][start_position[1]] = " "
        print("The delivery is late. Order is canceled.")
        break
    if matrix[new_row][new_col] == 'P':
        matrix[new_row][new_col] = 'R'
        current_position = [new_row, new_col]
        print("Pizza is collected. 10 minutes for delivery.")
        continue
    if matrix[new_row][new_col] == 'A':
        print("Pizza is delivered on time! Next order...")
        matrix[new_row][new_col] = 'P'
        break
    if matrix[new_row][new_col] == "*":
        continue
    if matrix[new_row][new_col] == "-":
        matrix[new_row][new_col] = "."

    current_position = [new_row, new_col]

for row in matrix:
    print(*row, sep="")
