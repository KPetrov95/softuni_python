from collections import deque


def battle(strike, monster):
    return strike - monster


monsters = deque(int(x) for x in input().split(","))
hero_strikes = [int(x) for x in input().split(",")]
killed_monsters = 0
while monsters and hero_strikes:
    current_monster = monsters.popleft()
    current_strike = hero_strikes.pop()
    if battle(current_strike, current_monster) >= 0:
        killed_monsters += 1
        if hero_strikes:
            hero_strikes[-1] += impact
        elif not hero_strikes and impact > 0:
            hero_strikes.append(impact)
    else:
        current_monster -= current_strike
        monsters.append(current_monster)
if not monsters:
    print("All monsters have been killed!")
if not hero_strikes:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")
