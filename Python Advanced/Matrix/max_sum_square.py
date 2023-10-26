from sys import maxsize

rows, cols = [int(x) for x in input().split(',')]

matrix = [[int(j) for j in input().split(', ')] for i in range(rows)]

max_square = -maxsize
max_square_nums = []

for i in range(rows - 1):
    for j in range(cols - 1):
        num = matrix[i][j]
        right = matrix[i][j + 1]
        bottom = matrix[i + 1][j]
        diagonal = matrix[i + 1][j + 1]
        sum_square = num + right + bottom + diagonal
        if sum_square > max_square:
            max_square = sum_square
            max_square_nums = [[num, right], [bottom, diagonal]]

print(*max_square_nums[0])
print(*max_square_nums[1])
print(max_square)
