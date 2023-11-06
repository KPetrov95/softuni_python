rows, cols = [int(x) for x in input().split()]

num = ord("a")

for i in range(rows):
    for j in range(cols):
        print(f"{chr((num + i))}{chr(num + i + j)}{chr(num + i)}", end=' ')

    print()