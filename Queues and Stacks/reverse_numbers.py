list_of_numbers = input().split()
second_list = []
for i in range(len(list_of_numbers)):
    second_list.append(int(list_of_numbers.pop()))

print(*second_list, end=" ")