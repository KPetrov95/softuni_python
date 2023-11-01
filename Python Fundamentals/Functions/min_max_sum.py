list_of_strings = input().split()
list_of_ints = []
for num in list_of_strings:
    list_of_ints.append(int(num))

print(f"The minimum number is {min(list_of_ints)}")
print(f"The maximum number is {max(list_of_ints)}")
print(f"The sum number is: {sum(list_of_ints)}")