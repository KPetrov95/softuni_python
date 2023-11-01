list_of_products = input().split()
bakery = {}

for index in range(0, len(list_of_products), 2):
    key = list_of_products[index]
    value = list_of_products[index + 1]
    bakery[key] = int(value)

    

