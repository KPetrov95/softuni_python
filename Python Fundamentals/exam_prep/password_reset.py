def take_odd(original_password):
    new_password = ''
    for char_index in range(1, len(original_password), 2):
        target_string = original_password[char_index]
        new_password += new_password.join(target_string)
    print(new_password)
    return new_password


def cut(original_password, data_list):
    index, length = data_list
    target_string = original_password[int(index):int(index)+int(length)] #dobavi +1 ako ne izliza
    original_password = original_password.replace(target_string, '', 1)
    print(original_password)
    return original_password


def substitute(original_password, data_list):
    substring, new_string = data_list
    if substring in original_password:
        original_password = original_password.replace(substring, new_string)
        print(original_password)
    else:
        print("Nothing to replace!")
    return original_password


def commands(original_password):
    while True:
        command, *data = input().split()
        if command == 'Done':
            print(f"Your password is: {original_password}")
            break
        elif command == 'TakeOdd':
            original_password = take_odd(original_password)
        elif command == 'Cut':
            original_password = cut(original_password, data)
        elif command == 'Substitute':
            original_password = substitute(original_password, data)


pass_word = input()

commands(pass_word)