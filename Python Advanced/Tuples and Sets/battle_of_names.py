n = int(input())

even_set = set()
odd_set = set()

for i in range(1, n + 1):
    name = input()
    value = sum([ord(x) for x in name]) // i

    if value % 2 == 0:
        even_set.add(value)
    else:
        odd_set.add(value)

if sum(even_set) == sum(odd_set):
    print(*even_set.union(odd_set), sep=', ')
elif sum(even_set) > sum(odd_set):
    print(*odd_set.symmetric_difference(even_set), sep=', ')
elif sum(even_set) < sum(odd_set):
    print(*odd_set.difference(even_set), sep=', ')