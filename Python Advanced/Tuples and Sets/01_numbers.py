set_one = set(int(x) for x in input().split())
set_two = set(int(x) for x in input().split())

n = int(input())

for i in range(n):
    line = input().split()
    command = line[0] + " " + line[1]
    nums = [int(x) for x in line[2:]]
    if command == 'Add First':
        set_one.update(nums)
    elif command == 'Add Second':
        set_two.update(nums)
    elif command == 'Remove First':
        set_one.difference_update(nums)
    elif command == 'Remove Second':
        set_two.difference_update(nums)
    elif command == 'Check Subset':
        print(set_one.issubset(set_two) or set_two.issubset(set_one))
print(*sorted(set_one), sep=', ')
print(*sorted(set_two), sep=', ')
