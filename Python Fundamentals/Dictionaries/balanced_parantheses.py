from collections import deque

sequence = deque(input())
opening = deque()

while sequence:
    left = sequence.popleft()
    if left in '({[':
        opening.append(left)
    elif not opening:
        print('NO')
        break
    else:
        if f'{opening.pop() + left}' not in '{}[]()':
            print('NO')
            break
else:
    print('YES')