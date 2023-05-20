lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

times_helmet_broken = lost_fights // 2
times_sword_broken = lost_fights // 3
times_shield_broken = lost_fights // (2 * 3)
times_armor_broken = lost_fights // (2 * 2 * 3)

expenses = times_helmet_broken * helmet_price +\
           times_sword_broken * sword_price +\
           times_shield_broken * shield_price +\
           times_armor_broken * armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")