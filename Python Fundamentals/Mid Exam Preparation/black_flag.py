days = int(input())
daily_plunder = int(input())
target_plunder = float(input())
collected_plunder = 0


for day in range(1, days + 1):
    collected_plunder += daily_plunder
    if day % 3 == 0:
        collected_plunder += 0.5 * daily_plunder
    if day % 5 == 0:
        collected_plunder -= 0.3 * collected_plunder

percentage = collected_plunder / target_plunder * 100

if collected_plunder >= target_plunder:
    print(f'Ahoy! {collected_plunder:.2f} plunder gained.')
else:
    print(f"Collected only {percentage:.2f}% of the plunder.")