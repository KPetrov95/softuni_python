from _collections import deque

supermarket_queue = deque()

while True:
    command = input()
    if command == 'End':
        print(f'{len(supermarket_queue)} people remaining.')
        break
    elif command == 'Paid':
        while len(supermarket_queue) > 0:
            customer_paid = supermarket_queue.popleft()
            print(customer_paid)
    else:
        supermarket_queue.append(command)
