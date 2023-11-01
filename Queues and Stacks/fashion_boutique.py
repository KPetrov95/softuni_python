clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
current_capacity = rack_capacity
rack = 1
while clothes:
    current_cloth = clothes.pop()
    if current_capacity < current_cloth:
        rack += 1
        current_capacity = rack_capacity
    current_capacity -= current_cloth
print(rack)

