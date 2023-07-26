def insert_space(encrypted_message, data):
    index = int(data[0])
    encrypted_message = encrypted_message[:index] + ' ' + encrypted_message[index:]
    print(encrypted_message)
    return encrypted_message


def reverse(encrypted_message, data):
    substring = data[0]
    if substring in encrypted_message:
        encrypted_message = encrypted_message.replace(substring, '', 1)
        encrypted_message += substring[::-1]
        print(encrypted_message)
    else:
        print("error")
    return encrypted_message


def change_all(encrypted_message, data):
    substring = data[0]
    replacement = data[1]
    if substring in encrypted_message:
        encrypted_message = encrypted_message.replace(substring, replacement)
        print(encrypted_message)
    return encrypted_message


def decrypt_message(encrypted_message):
    while True:
        command, *data_list = input().split(':|:')
        if command == "Reveal":
            print(f"You have a new text message: {encrypted_message}")
            break
        elif command == "InsertSpace":
            encrypted_message = insert_space(encrypted_message, data_list)
        elif command == "Reverse":
            encrypted_message = reverse(encrypted_message, data_list)
        elif command == "ChangeAll":
            encrypted_message = change_all(encrypted_message, data_list)



message = input()

decrypt_message(message)