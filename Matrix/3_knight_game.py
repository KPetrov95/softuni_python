n = int(input())

knights = []
matrix = []

for i in range(n):
    matrix.append([x for x in input()])
    for j in range(n):
        if matrix[i][j] == 'K':
            knights.append([i, j])

knight_moves = [(1, 2), (2, 1), (-1, 2), (1, -2), (-1, -2), (-2, -1), (2, -1), (-2, 1)]
removed_knights = 0

while True:
    max_hits = 0
    max_knight = [0, 0]
    for k_row, k_col in knights:
        hits = 0
        for move in knight_moves:
            new_row = k_row + move[0]
            new_col = k_col + move[1]
            if new_row in range(n) and new_col in range(n) and matrix[new_row][new_col] == 'K':
                hits += 1
        if hits > max_hits:
            max_hits = hits
            max_knight = [k_row, k_col]

    if max_hits == 0:
        break
    knights.remove(max_knight)
    matrix[max_knight[0]][max_knight[1]] = '0'
    removed_knights += 1

print(removed_knights)