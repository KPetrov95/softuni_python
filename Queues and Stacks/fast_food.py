from _collections import deque

available_food = int(input())
queue_of_orders = deque([int(x) for x in input().split()])
print(max(queue_of_orders))
while queue_of_orders:
    current_order = queue_of_orders.popleft()
    if available_food >= current_order:
        available_food -= current_order
    else:
        queue_of_orders.appendleft(current_order)
        print(f'Orders left: ', end='')
        print(*queue_of_orders, sep=' ')
        break
else:
    print("Orders complete")