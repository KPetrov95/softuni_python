first_string = input()
second_string = input()

current_string = first_string

for char in range(len(first_string)):

    left_side = second_string[: char + 1]
    right_side = first_string[char + 1:]

    new_string = left_side + right_side
    if new_string != current_string:
        print(new_string)
        current_string = new_string
