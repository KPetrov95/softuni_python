n = int(input())

longest = []

for i in range(n):
    first_set = set()
    second_set = set()
    set_one, set_two = input().split('-')
    set_one_start, set_one_end = set_one.split(',')
    set_two_start, set_two_end = set_two.split(',')
    for num in range(int(set_one_start), int(set_one_end) + 1):
        first_set.add(num)
    for num_two in range(int(set_two_start), int(set_two_end) + 1):
        second_set.add(num_two)
    intersection = first_set.intersection(second_set)
    if len(intersection) > len(longest):
        longest = list(intersection)

print(f'Longest intersection is {longest} with length {len(longest)}')