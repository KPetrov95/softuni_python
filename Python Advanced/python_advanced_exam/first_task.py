from collections import deque

initial_fuel = deque(int(x) for x in input().split())
additional_consumption_index = deque(int(x) for x in input().split())
needed_fuel = deque(int(x) for x in input().split())
altitude_count = 0
reached_altitudes = deque()
reached_top = False
result = ''
while needed_fuel:
    altitude_count += 1
    current_fuel = initial_fuel.pop()
    current_index = additional_consumption_index.popleft()
    current_altitude = needed_fuel.popleft()
    available_fuel = current_fuel - current_index
    if available_fuel >= current_altitude:
        reached_altitudes.append(f'Altitude {altitude_count}')
        print(f'John has reached: Altitude {altitude_count}')
    else:
        print(f"John did not reach: Altitude {altitude_count}")
        break
else:
    reached_top = True
    result += "John has reached all the altitudes and managed to reach the top!"

if not reached_top:
    result += 'John failed to reach the top.\n'
    if reached_altitudes:
        result += 'Reached altitudes: '
        result += ', '.join(reached_altitudes)
    else:
        result += "John didn't reach any altitude."

print(result)