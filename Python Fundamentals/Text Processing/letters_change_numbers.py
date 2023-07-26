some_strings = input().split()
final_sum = 0

for current_string in some_strings:
    first_letter = current_string[0]
    final_letter = current_string[-1]
    num = int(current_string[1:len(current_string) -1])

    if first_letter.isupper():
        first_letter_position = ord(first_letter) - 64
        final_sum += num / first_letter_position
    elif first_letter.islower():
        first_letter_position = ord(first_letter) - 96
        final_sum += num * first_letter_position
    if final_letter.isupper():
        final_letter_position = ord(final_letter) - 64
        final_sum -= final_letter_position
    elif final_letter.islower():
        final_letter_position = ord(final_letter) - 96
        final_sum += final_letter_position

print(f'{final_sum:.2f}')