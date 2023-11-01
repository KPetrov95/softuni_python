list_of_strings = input().split()
list_of_ints = []
for num in list_of_strings:
    list_of_ints.append(int(num))

print(sorted(list_of_ints))