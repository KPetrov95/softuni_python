rows, cols = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split()] for i in range(rows)]

sum_cols = 0

for row_index in range(cols):
    for col_index in range(rows):
        sum_cols += matrix[col_index][row_index]
    print(sum_cols)
    sum_cols = 0
