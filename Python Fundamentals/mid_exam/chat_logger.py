command = input()
chat_list = []

while command != 'end':
    command = command.split()
    if command[0] == 'Chat':
        chat_list.append(command[1])
    elif command[0] == 'Delete':
        if command[1] in chat_list:
            chat_list.remove(command[1])
    elif command[0] == 'Edit':
        if command[1] in chat_list:
            index_to_edit = chat_list.index(command[1])
            chat_list[index_to_edit] = command[2]
    elif command[0] == 'Pin':
        if command[1] in chat_list:
            chat_list.remove(command[1])
            chat_list.append(command[1])
    elif command[0] == 'Spam':
        for x in range(1, len(command)):
            chat_list.append(command[x])
    command = input()

print("\n".join(chat_list))