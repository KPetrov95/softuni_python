from collections import deque

color_strings = deque(input().split())

primary_colours =['red', 'blue', 'yellow']
secondary_colours ={'orange': ['red', 'yellow'],
                    'purple': ['red', 'blue'],
                    'green': ['blue', 'yellow'],
                    }
obtained_colours = []

while color_strings:
    first_string = color_strings.popleft()
    if color_strings:
        last_string = color_strings.pop()
    else:
        last_string = ""
    potential_colour_one = first_string + last_string
    potential_colour_two = last_string + first_string
    if potential_colour_one in primary_colours or potential_colour_one in secondary_colours:
        obtained_colours.append(potential_colour_one)
    elif potential_colour_two in primary_colours or potential_colour_two in secondary_colours:
        obtained_colours.append(potential_colour_two)
    else:
        if len(first_string) > 1:
            color_strings.insert(len(color_strings) // 2, first_string[:-1])
        if len(last_string) > 1:
            color_strings.insert(len(color_strings) // 2, last_string[:-1])

for colour in obtained_colours:
    if colour in secondary_colours:
        for element in secondary_colours[colour]:
            if element not in obtained_colours:
                obtained_colours.remove(colour)

print(obtained_colours)