n = int(input())

matrix = []
alice = []

for i in range(n):
    matrix.append([x for x in input().split()])
    for j in range(n):
        if matrix[i][j] == 'A':
            alice = [i, j]
            matrix[i][j] = '*'

possible_moves = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
tea_bags = 0

while tea_bags < 10:
    command = input()
    new_row = possible_moves[command][0] + alice[0]
    new_column = possible_moves[command][1] + alice[1]
    if new_row not in range(n) or new_column not in range(n):
        break
    elif matrix[new_row][new_column] == 'R':
        matrix[new_row][new_column] = '*'
        break
    elif matrix[new_row][new_column].isnumeric():
        tea_bags += int(matrix[new_row][new_column])
    matrix[new_row][new_column] = '*'
    alice = [new_row, new_column]
if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")
for row in matrix:
    print(*row)
