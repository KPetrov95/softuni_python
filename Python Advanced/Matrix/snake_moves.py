from collections import deque

r, c = [int(x) for x in input().split()]

phrase = deque(input())

matrix = []

for row in range(r):
    matrix.append([''] * c )
    for col in range(c):
        if row % 2 == 0:
            matrix[row][col] = phrase[0]
        else:
            matrix[row][-1 - col] = phrase[0]
        phrase.rotate(-1)
[print(*row, sep='') for row in matrix]