n = int(input())

matrix = [[int(x) for x in input().split()] for i in range(n)]

while True:
    command, *data = input().split()
    if command == 'END':
        break
    r, c, v = [int(x) for x in data]
    if r in range(n) and c in range(n):
        if command == 'Add':
            matrix[r][c] += v
        elif command == 'Subtract':
            matrix[r][c] -= v
    else:
        print("Invalid coordinates")

for row in matrix:
    print(*row)