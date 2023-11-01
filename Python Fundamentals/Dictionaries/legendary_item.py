items = {'shards': 0, 'fragments': 0, 'motes': 0}
obtained = False
legendary_item = ''
while not obtained:
    current_items = input().split()
    for index in range(0, len(current_items), 2):
        quantity = int(current_items[index])
        material = current_items[index + 1].lower()
        if material not in items:
            items[material] = 0
        items[material] += quantity
        if items['shards'] >= 250:
            items['shards'] -= 250
            obtained = True
            legendary_item = 'Shadowmourne'
        elif items['fragments'] >= 250:
            items['fragments'] -= 250
            obtained = True
            legendary_item = 'Valanyr'
        elif items['motes'] >= 250:
            items['motes'] -= 250
            obtained = True
            legendary_item = 'Dragonwrath'
        if obtained:
            print(f"{legendary_item} obtained!")
            break
    if obtained:
        break
for item, quantity in items.items():
    print(f"{item}: {quantity}")
