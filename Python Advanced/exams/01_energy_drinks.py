from collections import deque

milligrams_of_caffeine = deque(int(x) for x in input().split(', '))
energy_drinks = deque(int(x) for x in input().split(', '))

MAX_CAFFEINE = 300
current_caffeine = 0

while milligrams_of_caffeine and energy_drinks:
    current_milligrams = milligrams_of_caffeine.pop()
    current_drink = energy_drinks.popleft()
    caffeine = current_milligrams * current_drink
    if caffeine + current_caffeine <= MAX_CAFFEINE:
        current_caffeine += caffeine
    else:
        energy_drinks.append(current_drink)
        current_caffeine -= 30
        if current_caffeine < 0:
            current_caffeine = 0
if energy_drinks:
    print(f'Drinks left: {", ".join(str(x) for x in energy_drinks)}')
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {current_caffeine} mg caffeine.")