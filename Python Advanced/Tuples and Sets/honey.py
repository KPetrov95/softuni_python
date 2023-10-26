from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

operators = {
    "+": lambda b, n: b + n,
    "-": lambda b, n: b - n,
    "/": lambda b, n: b / n,
    "*": lambda b, n: b * n,
}

honey = 0

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()
    if current_nectar < current_bee:
        bees.appendleft(current_bee)
        continue
    else:
        used_symbol = symbols.popleft()
        # if used_symbol == '+':
        #     honey += abs(current_bee + current_nectar)
        # elif used_symbol == '-':
        #     honey += abs(current_bee - current_nectar)
        # elif used_symbol == '*':
        #     honey += abs(current_bee * current_nectar)
        # elif used_symbol == '/' and current_nectar > 0:
        #     honey += abs(current_bee / current_nectar)
        if current_nectar != 0:
            honey += abs(operators[used_symbol](current_bee, current_nectar))

print(f'Total honey made: {honey}')
if bees:
    print(f'Bees left: {", ".join(str(x) for x in bees)}')
if nectar:
    print(f'Nectar left: {", ".join(str(x) for x in nectar)}')
