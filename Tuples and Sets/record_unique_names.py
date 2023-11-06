n = int(input())

unique_names = set()

for _ in range(n):
    name = input()
    unique_names.add(name)

for unique_name in unique_names:
    print(unique_name)