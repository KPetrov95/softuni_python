rows = int(input())
matrix = [[j for j in input()] for i in range(rows)]
target_symbol = input()

for i in range(rows):
    for j in range(len(matrix[i])):
        if matrix[i][j] == target_symbol:
            position = (i, j)
            print(position)
            exit()
print(f"{target_symbol} does not occur in the matrix")