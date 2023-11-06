rows = int(input())
matrix = [[int(j) for j in input().split()] for i in range(rows)]
sum_diag = 0

for i in range(rows):
    sum_diag += matrix[i][i]

print(sum_diag)