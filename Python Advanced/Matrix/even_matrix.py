rows = int(input())
matrix = []

for row_index in range(rows):
    elements = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
    matrix.append(elements)
print(matrix)