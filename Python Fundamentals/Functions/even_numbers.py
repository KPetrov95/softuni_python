def even_numbers_filter(number):
    if number % 2 == 0:
        return True


list_of_strings = input().split()
list_of_ints = []
for num in list_of_strings:
    list_of_ints.append(int(num))

result = list(filter(even_numbers_filter, list_of_ints))
print(result)
