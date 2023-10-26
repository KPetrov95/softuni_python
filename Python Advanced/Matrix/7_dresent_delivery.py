m = int(input())  # number of presents
n = int(input())  # number of rows and cols

matrix = []
current_position = []
nice_kids = 0

for i in range(n):
    matrix.append(input().split())
    for j in range(n):
        if matrix[i][j] == 'S':
            current_position = [i, j]
        elif matrix[i][j] == 'V':
            nice_kids += 1
count_nice_kids = nice_kids
possible_moves = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
command = input()

while command != "Christmas morning":
    new_row = current_position[0] + possible_moves[command][0]
    new_col = current_position[1] + possible_moves[command][1]
    if new_row in range(n) and new_col in range(n):
        if matrix[new_row][new_col] == "V":
            m -= 1
            nice_kids -= 1
            matrix[new_row][new_col] = "-"
        elif matrix[new_row][new_col] == "C":
            for key, value in possible_moves.items():
                next_row = new_row + value[0]
                next_col = new_col + value[1]
                if next_row in range(n) and next_col in range(n):
                    if matrix[next_row][next_col] == "V":
                        nice_kids -= 1
                        m -= 1
                        matrix[next_row][next_col] = "-"
                    elif matrix[next_row][next_col] == "X":
                        m -= 1
                        matrix[next_row][next_col] = "-"
        matrix[current_position[0]][current_position[1]] = '-'
        current_position = [new_row, new_col]
        matrix[current_position[0]][current_position[1]] = 'S'
        if nice_kids <= 0:
            break
        if m == 0:
            print("Santa ran out of presents!")
            break

    command = input()
for row in matrix:
    print(*row)
if nice_kids == 0:
    print(f"Good job, Santa! {count_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")
