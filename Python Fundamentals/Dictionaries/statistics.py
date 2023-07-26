
bakery = {}
while True:
    command = input()
    if command == 'statistics':
        break
    list_of_products = command.split(': ')
    key = list_of_products[0]
    value = list_of_products[1]
    if key not in bakery:
        bakery[key] = int(value)
    else:
        bakery[key] += int(value)

print('Products in stock:')
for key, value in bakery.items():
    print(f'- {key}: {value}')

total_products = len(bakery)
quantity = sum(bakery.values())
print(f'Total Products: {total_products}')
print(f'Total Quantity: {quantity}')