list_of_gifts = input().split()

command = input()

while command != 'No Money':

    type_of_gift = command.split()
    status_of_gift = type_of_gift[0]
    gift_item = type_of_gift[1]
    if status_of_gift == 'OutOfStock':

        if gift_item in list_of_gifts:
            gift_item = None
    elif status_of_gift == 'Required':
        index_of_gift = int(type_of_gift[2])
        if 0 <= index_of_gift < len(list_of_gifts) - 1:
            list_of_gifts[index_of_gift] = gift_item
    elif status_of_gift == 'JustInCase':
        list_of_gifts[-1] = gift_item
    command = input()

for item in list_of_gifts:
    if item != "None":
        print(item, end=" ")

