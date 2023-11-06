from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())
toys = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}
created_presents = {}

while magic and materials:
    total_magic = materials[-1] * magic[0]
    if total_magic in toys:
        if toys[total_magic] not in created_presents:
            created_presents[toys[total_magic]] = 0
        created_presents[toys[total_magic]] += 1
        materials.pop()
        magic.popleft()
    elif total_magic < 0:
        materials.append(materials.pop() + magic.popleft())
    elif total_magic > 0:
        magic.popleft()
        materials[-1] += 15
    elif magic[0] == 0 and materials[-1] == 0:
        magic.popleft()
        materials.pop()
    elif magic[0] == 0:
        magic.popleft()
    elif materials[-1] == 0:
        materials.pop()
if ('Doll' in created_presents and 'Wooden train' in created_presents) or ('Teddy bear' in created_presents and 'Bicycle' in created_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")
for key, value in sorted(created_presents.items()):
    print(f'{key}: {value}')
