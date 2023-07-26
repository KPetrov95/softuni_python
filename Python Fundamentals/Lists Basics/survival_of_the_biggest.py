list_of_strings = input().split()
numbers_to_remove = int(input())
list_of_ints = []
sorted_list = []
for element in list_of_strings:
    list_of_ints.append(int(element))
    sorted_list.append(int(element))

sorted_list.sort(reverse=True)

for current_number in range(numbers_to_remove):
    smallest_number = sorted_list.pop(-1)
    if smallest_number in list_of_ints:
        list_of_ints.remove(smallest_number)

print(*list_of_ints, sep=', ')
