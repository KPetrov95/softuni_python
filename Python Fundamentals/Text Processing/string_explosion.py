string = input()
explosion_strength = 0
final_string = ""
for index in range(len(string)):
    if string[index] != '>' and explosion_strength > 0:
        explosion_strength -= 1
    elif string[index] == '>':
        final_string += string[index]
        explosion_strength += int(string[index + 1])
    else:
        final_string += string[index]

print(final_string)