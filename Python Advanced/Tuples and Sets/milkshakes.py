from collections import deque

chocolate = [int(x) for x in input().split(', ')]
milk = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while milkshakes < 5 and milk and chocolate:
    current_chocolate = chocolate.pop()
    current_milk = milk.popleft()
    if current_chocolate == current_milk:
        milkshakes += 1
    else:
        if current_milk <= 0:
            chocolate.append(current_chocolate)
            continue
        if current_chocolate <= 0:
            milk.appendleft(current_milk)
            continue
        milk.append(current_milk)
        chocolate.append(current_chocolate - 5)

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print("Not enough milkshakes.")
print(f'Chocolate: {", ".join(str(x) for x in chocolate) if chocolate else "empty"}')
print(f'Milk: {", ".join(str(x) for x in milk) if milk else "empty"}')
