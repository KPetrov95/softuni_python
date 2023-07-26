list_of_items = input().split(', ')


while True:
    command = input()
    if command == 'Craft!':
        break
    action, item = command.split(' - ')

    if action == 'Collect':
        if item not in list_of_items:
            list_of_items.append(item)
    elif action == 'Drop':
        if item in list_of_items:
            list_of_items.remove(item)
    elif action == 'Renew':
        if item in list_of_items:
            list_of_items.remove(item)
            list_of_items.append(item)
    elif action == 'Combine Items':
        first_item, second_item = item.split(':')
        if first_item in list_of_items:
            old_item_index = list_of_items.index(first_item)
            list_of_items.insert(old_item_index + 1, second_item)

print(', '.join(list_of_items))