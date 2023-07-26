needed_exp = float(input())
count_of_battles = int(input())

total_battles = 0
gained_exp = 0
reached_tank = False

for battle in range(count_of_battles):
    total_battles += 1
    current_battle = float(input())
    if total_battles % 3 == 0:
        current_battle *= 1.15
    if total_battles % 5 == 0:
        current_battle *= 0.9
    if total_battles % 15 == 0:
        current_battle *= 1.05
    gained_exp += current_battle
    if gained_exp >= needed_exp:
        reached_tank = True
        break
difference = needed_exp - gained_exp
if reached_tank:
    print(f"Player successfully collected his needed experience for {total_battles} battles.")
else:
    print(f"Player was not able to collect the needed experience, {difference:.2f} more needed.")