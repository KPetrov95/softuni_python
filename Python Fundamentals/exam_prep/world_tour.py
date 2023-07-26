def add_stop(destinations, index_to_use, string_to_use):
    if index_to_use in range(len(destinations)):
        destinations = destinations[:index_to_use] + string_to_use + destinations[index_to_use:]
    return destinations


def remove_stop(destinations, first_index, second_index):
    if first_index in range(len(destinations)) and second_index in range(len(destinations)):
        destinations = destinations[:first_index] + destinations[second_index + 1:]
    return destinations


def switch_stop(destinations, old_destination, new_destination):
    if old_destination in destinations:
        destinations = destinations.replace(old_destination, new_destination)
    return destinations


all_stops = input()

while True:
    command = input().split(':')
    if command[0] == 'Travel':
        break
    elif command[0] == 'Add Stop':
        index_string = int(command[1])
        destination_string = command[2]
        all_stops = add_stop(all_stops, index_string, destination_string)
    elif command[0] == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[2])
        all_stops = remove_stop(all_stops, start_index, end_index)
    elif command[0] == 'Switch':
        old_string = command[1]
        new_string = command[2]
        all_stops = switch_stop(all_stops, old_string, new_string)
    print(all_stops)

print(f"Ready for world tour! Planned stops: {all_stops}")