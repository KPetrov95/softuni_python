MAX_LENGTH = 5

list_of_numbers = [int(x) for x in input().split()]
average_num = sum(list_of_numbers) / len(list_of_numbers)
filtered_list = sorted([x for x in list_of_numbers if x > average_num])

if not filtered_list:
    print("No")
else:
    print(*[filtered_list.pop() for i in range(MAX_LENGTH) if filtered_list])