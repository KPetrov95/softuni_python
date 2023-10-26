numbers = tuple(float(x) for x in input().split())

occurrences = {}

for num in numbers:
    occurrences[num] = numbers.count(num)

for key, value in occurrences.items():
    print(f'{key} - {value} times')