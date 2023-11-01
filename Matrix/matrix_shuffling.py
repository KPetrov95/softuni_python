def is_valid(r1, c1, r2, c2, rs, cs):
    return 0 <= r1 <= rs and 0 <= r2 <= rs and 0 <= c1 <= cs and 0 <= c2 <= cs


rows, cols = [int(x) for x in input().split()]

matrix = [[int(j) for j in input().split()]for i in range(rows)]

while True:
    command = input()
    if command == 'END':
        break
    line = command.split()
    if line[0] != 'swap' or len(line) != 5:
        print("Invalid input!")
        continue
    row_one, col_one, row_two, col_two = [int(x) for x in line[1:]]
    if is_valid(row_one, col_one, row_two, col_two, rows, cols):
        matrix[row_one][col_one], matrix[row_two][col_two] = matrix[row_two][col_two], matrix[row_one][col_one]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")
        continue
