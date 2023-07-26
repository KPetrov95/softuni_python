targets = [int(x) for x in input().split()]

command = input()

while command != 'End':
    target_index = int(command)
    for num in range(len(targets)):
        if target_index >= len(targets):
            continue

        elif targets[target_index] > targets[num] != -1:
            targets[num] += targets[target_index]
        elif targets[target_index] < targets[num] != -1:
            targets[num] -= targets[target_index]
        targets[target_index] = -1

    command = input()

print(targets)