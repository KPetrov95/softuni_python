def shop_from_grocery_list(budget, grocery_list, *items):
    bought_items = []
    for product, price in items:
        if product in grocery_list and product not in bought_items:
            if price <= budget:
                grocery_list.remove(product)
                budget -= price
                bought_items.append(product)
            else:
                break
    if grocery_list:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."
    return f"Shopping is successful. Remaining budget: {budget:.2f}."

print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
print()

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))

