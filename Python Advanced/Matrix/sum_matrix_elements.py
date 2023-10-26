rows, cols = [int(x) for x in input().split(', ')]
matrix = []
sums = 0
for col_index in range(rows):
    elements = [int(x) for x in input().split(', ')]
    sums += sum(elements)
    matrix.append(elements)

print(sums)
print(matrix)