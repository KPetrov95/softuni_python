list_of_string = input().split()
list_of_floats = []

for num in list_of_string:
    list_of_floats.append(round(float(num)))

print(list_of_floats)