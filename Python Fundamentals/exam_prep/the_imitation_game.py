def move(msg, number):
    msg = msg[number:] + msg[:number]
    return msg


def insert(msg, number, character):
    msg = msg[:number] + character + msg[number:]
    return msg


def change_all(msg, old_char, new_char):
    msg = msg.replace(old_char, new_char)
    return msg


message = input()

while True:
    command = input()
    if command == 'Decode':
        print(f"The decrypted message is: {message}")
        break
    command = command.split('|')
    if command[0] == 'Move':
        letters_to_move = int(command[1])
        message = move(message, letters_to_move)
    elif command[0] == 'Insert':
        index_to_insert = int(command[1])
        letter_to_insert = command[2]
        message = insert(message, index_to_insert, letter_to_insert)
    elif command[0] == 'ChangeAll':
        old_letter = command[1]
        new_letter = command[2]
        message = change_all(message, old_letter, new_letter)
