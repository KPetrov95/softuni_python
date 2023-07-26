list_of_nums = [int(x) for x in input().split()]
command = input()

while command != 'end':
    if command == 'decrease':
        list_of_nums = [x - 1 for x in list_of_nums]
    else:
        function, index_one, index_two = [x if x.isalpha() else int(x) for x in command.split()]
        index_one = int(index_one)
        index_two = int(index_two)
        if function == 'swap':
            list_of_nums[index_one], list_of_nums[index_two] = list_of_nums[index_two], list_of_nums[index_one]
        elif function == 'multiply':
            list_of_nums[index_one] = list_of_nums[index_one] * list_of_nums[index_two]

    command = input()

print(*list_of_nums,sep=', ')