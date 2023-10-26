rows, cols = [int(x) for x in input().split()]

matrix = [[int(j) for j in input().split()] for i in range(rows)]

max_sum = float('-inf')
max_row = 0
max_col = 0

for i in range(rows - 2):
    for j in range(cols - 2):
        current_sum = 0
        for r in range(i, i + 3):
            for c in range(j, j + 3):
                current_sum += matrix[r][c]
        if current_sum > max_sum:
            max_sum = current_sum
            max_row = i
            max_col = j

print(f"Sum = {max_sum}")

max_matrix =[matrix[i][max_col:max_col + 3] for i in range(max_row, max_row + 3)]
[print(*row) for row in max_matrix]