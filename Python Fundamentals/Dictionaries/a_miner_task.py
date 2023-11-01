resources = {}

while True:
    key = input()
    if key == 'stop':
        break
    amount = int(input())
    if key not in resources:
        resources[key] = 0
    resources[key] += amount

for keys, amounts in resources.items():
    print(f'{keys} -> {amounts}')