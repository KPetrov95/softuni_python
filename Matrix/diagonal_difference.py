matrix =[[int(i) for i in input().split()]for j in range(int(input()))]
primary_diagonal = []
secondary_diagonal = []
for row in range(len(matrix)):
    col = len(matrix) - row - 1
    secondary_element = matrix[row][col]
    secondary_diagonal.append(secondary_element)
    primary_diagonal.append(matrix[row][row])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))