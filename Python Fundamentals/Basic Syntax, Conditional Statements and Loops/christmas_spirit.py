quantity_per_shopping = int(input())
days_remaining_until_christmas = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

christmas_spirit = 0
budget = 0
for day in range(1, days_remaining_until_christmas + 1):

    if day % 11 == 0:
        quantity_per_shopping += 2

    if day % 2 == 0:
        budget += quantity_per_shopping * 2
        christmas_spirit += 5
    if day % 3 == 0:
        budget += quantity_per_shopping * (tree_garland_price + tree_skirt_price)
        christmas_spirit += 13
    if day % 5 == 0:
        budget += quantity_per_shopping * 15
        christmas_spirit += 17
        if day % 3 ==0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        budget += tree_lights_price + tree_skirt_price + tree_garland_price
if days_remaining_until_christmas % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {christmas_spirit}")