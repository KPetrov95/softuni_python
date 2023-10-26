n, m = [int(x) for x in input().split()]

first_set = set()
second_set = set()

for i in range(n):
    first_set.add(input())

for i in range(m):
    second_set.add(input())

unique_elements = first_set.intersection(second_set)

for element in unique_elements:
    print(element)