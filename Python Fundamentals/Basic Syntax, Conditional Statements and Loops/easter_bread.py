budget = float(input())
price_for_kg_flour = float(input())

price_for_pack_of_eggs = price_for_kg_flour * 0.75
price_for_liter_milk = price_for_kg_flour * 1.25

colored_eggs = 0
current_bread_count = 0
price_for_one_bread = price_for_kg_flour + price_for_pack_of_eggs + price_for_liter_milk / 4

while budget > price_for_one_bread:
    #if price_for_one_bread > budget:
    #    break
    budget -= price_for_one_bread
    current_bread_count += 1
    colored_eggs += 3

    if current_bread_count % 3 == 0:
        colored_eggs -= current_bread_count - 2

print(f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
