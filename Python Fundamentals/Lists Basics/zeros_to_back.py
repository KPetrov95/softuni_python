list_of_nums = input().split(", ")
list_of_ints = []

for index, element in enumerate(list_of_nums:-1:-1):
    element = int(element)
    if element == 0:
        list_of_ints.insert(-1, element)
    else:
        list_of_ints.insert(index, element)

print(list_of_nums)
print(list_of_ints)