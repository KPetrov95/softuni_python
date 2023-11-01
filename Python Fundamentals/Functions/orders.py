def order(type_of_order, num):
    if type_of_order == "coffee":
        return 1.50 * num
    elif type_of_order == "coke":
        return 1.40 * num
    elif type_of_order == "water":
        return num
    elif type_of_order == "snacks":
        return 2.00 * num


product = input()
quantity = int(input())
print(f'{order(product, quantity):.2f}')