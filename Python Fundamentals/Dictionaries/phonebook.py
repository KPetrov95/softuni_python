phonebook = {}
command = input()
while "-" in command:
    name, number = command.split("-")
    phonebook[name] = number
    command = input()
for index in range(int(command)):
    person = input()
    if person in phonebook:
        print(f'{person} -> {phonebook[person]}')
    else:
        print(f'Contact {person} does not exist.')

