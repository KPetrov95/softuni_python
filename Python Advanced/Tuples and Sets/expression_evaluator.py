from collections import deque

expression = input().split()
numbers = deque()

for symbol in expression:
    if symbol not in "*/+-":
        numbers.append(symbol)
    else:
        while len(numbers) > 1:
            first_number = int(numbers.popleft())
            second_number = int(numbers.popleft())
            if symbol == "*":
                numbers.appendleft(first_number * second_number)
            elif symbol == "/":
                numbers.appendleft(first_number // second_number)
            elif symbol == "+":
                numbers.appendleft(first_number + second_number)
            elif symbol == "-":
                numbers.appendleft(first_number - second_number)

print(int(numbers.popleft()))