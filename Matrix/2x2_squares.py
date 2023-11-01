rows, cols = [int(x) for x in input().split()]

matrix = [[j for j in input().split()] for i in range(rows)]
counter = 0

for i in range(rows - 1):
    for j in range(cols - 1):
        first = matrix[i][j]
        second = matrix[i][j + 1]
        third = matrix[i + 1][j]
        fourth = matrix[i + 1][j + 1]

        if first == second == third == fourth:
            counter += 1
print(counter)