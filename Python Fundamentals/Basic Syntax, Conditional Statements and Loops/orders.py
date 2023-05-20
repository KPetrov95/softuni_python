number_of_orders = int(input())
total_price = 0
for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_per_capsule > 100 or price_per_capsule < 0.01:
        continue
    elif days > 31 or days <= 0:
        continue
    elif capsules_per_day > 2000 or capsules_per_day <= 0:
        continue
    price_for_order = price_per_capsule * days * capsules_per_day
    total_price += price_for_order
    print(f"The price for the coffee is: ${price_for_order:.2f}")

print(f"Total: ${total_price:.2f}")