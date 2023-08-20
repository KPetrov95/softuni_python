def translate(string_a, values):
    char, replacement = values
    string_a = string_a.replace(char, replacement)
    print(string_a)
    return string_a

def includes(string_a, values):
    substring = "".join(values)
    if substring in string_a:
        print('True')
    else:
        print('False')
    return string_a

def start(string_a, values):
    substring = "".join(values)
    if string_a.startswith(substring):
        print('True')
    else:
        print('False')
    return string_a



def lowercase(string_a):
    string_a = string_a.lower()
    print(string_a)
    return string_a

def findindex(string_a, values):
    substring = "".join(values)
    target_index = 0
    for current_index in range(len(string_a)):
        if string_a[current_index] == substring:
            target_index = current_index
    print(target_index)
    return string_a


def remove(string_a, values):
    start_index, count = values
    start_index = int(start_index)
    count = int(count)
    string_a = string_a[:start_index] + string_a[start_index + count:]
    print(string_a)
    return string_a

initial_string = input()

while True:
    command, *data = input().split()
    if command == 'End':
        break
    elif command == 'Translate':
        initial_string = translate(initial_string, data)
    elif command == 'Includes':
        initial_string = includes(initial_string, data)
    elif command == 'Start':
        initial_string = start(initial_string, data)
    elif command == 'Lowercase':
        initial_string = lowercase(initial_string)
    elif command == 'FindIndex':
        initial_string = findindex(initial_string, data)
    elif command == 'Remove':
        initial_string = remove(initial_string, data)
