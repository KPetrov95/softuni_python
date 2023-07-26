def ascii_characters(first_char, second_char):
    list_of_chars = []
    start_point = ord(first_char)
    end_point = ord(second_char)
    for char in range(start_point + 1, end_point):
        list_of_chars.append(chr(char))
    return list_of_chars


char_one = input()
char_two = input()
result = ascii_characters(char_one, char_two)
print(' '.join(result))
