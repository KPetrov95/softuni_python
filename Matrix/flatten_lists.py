matrix = [[int(j) for j in i.split()] for i in reversed(input().split('|')) ]

flattened_matrix = []

for i in range(len(matrix)):
    for j in matrix[i]:
        flattened_matrix.append(j)
print(*flattened_matrix)
