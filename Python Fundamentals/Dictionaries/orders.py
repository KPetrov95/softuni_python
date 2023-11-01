products = {}

while True:
    command = input().split()
    if command[0] == 'buy':
        break
    product, price, quantity = command[0], float(command[1]), int(command[2])
    if product not in products.keys():
        products[product] = [price, quantity]
    else:
        products[product][0] = price
        products[product][1] += quantity

for key, value in products.items():
    final_price = value[0] * value[1]
    print(f'{key} -> {final_price:.2f}')