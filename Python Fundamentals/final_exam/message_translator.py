import re

number_of_strings = int(input())
pattern = r'!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]'

for current_string_index in range(number_of_strings):
    current_string = input()
    result = re.findall(pattern, current_string)
    if not result:
        print("The message is invalid")
    else:
        valid_string = result[0]
        command, message = valid_string
        new_string = []
        for char in message:
            new_string.append(str((ord(char))))
        print(f'{command}: {" ".join(new_string)}')