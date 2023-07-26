list_of_products = input().split()
bakery = {}
products_to_check = input().split()

for index in range(0, len(list_of_products), 2):
    key = list_of_products[index]
    value = list_of_products[index + 1]
    bakery[key] = int(value)

for current_product in products_to_check:
    if current_product in bakery:
        print(f"We have {bakery[current_product]} of {current_product} left")
    else:
        print(f"Sorry, we don't have {current_product}")
