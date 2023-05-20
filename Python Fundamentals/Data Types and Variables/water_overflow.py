number_of_lines = int(input())

water_tank_capacity = 255
total_water_poured = 0

for pourings_of_water in range(number_of_lines):
    current_water_pouring = int(input())
    if water_tank_capacity < current_water_pouring:
        print("Insufficient capacity!")
        continue
    total_water_poured += current_water_pouring
    water_tank_capacity -= current_water_pouring

print(total_water_poured)