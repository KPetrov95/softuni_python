initial_values = input().split()
int_values = []
for value in initial_values:
    value = float(value)
    int_values.append(abs(value))

print(int_values)