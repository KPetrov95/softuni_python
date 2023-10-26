matrix =[[int(i) for i in input().split(', ')]for j in range(int(input()))]
primary_diagonal = []
secondary_diagonal = []
for row in range(len(matrix)):
    col = len(matrix) - row - 1
    secondary_diagonal.append(matrix[row][col])
    primary_diagonal.append(matrix[row][row])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")