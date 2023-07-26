sequence_of_elements = input().split()
number_of_moves = 0
command = input()
while command != 'end':
    first_index, second_index = [int(x) for x in command.split()]
    number_of_moves += 1
    element_to_add = f'-{number_of_moves}a'
    valid_input = True
    middle_of_the_list = len(sequence_of_elements) // 2

    if first_index == second_index or not 0 <= first_index < len(sequence_of_elements) or not 0 <= second_index < len(sequence_of_elements):
        valid_input = False

    if valid_input:
        if sequence_of_elements[first_index] == sequence_of_elements[second_index]:
            print(f"Congrats! You have found matching elements - {sequence_of_elements[first_index]}!")
            del sequence_of_elements[first_index]
            if first_index < second_index:
                second_index -= 1
            del sequence_of_elements[second_index]
        elif sequence_of_elements[first_index] != sequence_of_elements[second_index]:
            print("Try again!")
    else:
        sequence_of_elements = sequence_of_elements[:middle_of_the_list] + [element_to_add, element_to_add] + \
                               sequence_of_elements[middle_of_the_list:]
        print("Invalid input! Adding additional elements to the board")
    if not sequence_of_elements:
        break
    command = input()

if sequence_of_elements:
    print('Sorry you lose :(')
    print(*sequence_of_elements)
else:
    print(f'You have won in {number_of_moves} turns!')
