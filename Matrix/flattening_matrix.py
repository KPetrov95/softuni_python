rows = int(input())

matrix = []
flat = []

for row_index in range(rows):
    elements = [int(x) for x in input().split(', ')]
    matrix.append(elements)

for row_index in range(rows):
    for col_index in range(len(matrix[row_index])):
        element = matrix[row_index][col_index]
        flat.append(element)
print(flat)