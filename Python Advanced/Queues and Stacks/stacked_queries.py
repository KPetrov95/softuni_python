number_of_lines = int(input())
stack = []

for i in range(number_of_lines):
    numbers = input().split()
    if numbers[0] == '1':
        stack.append(int(numbers[1]))
    elif stack:
        if numbers[0] == '2':
            stack.pop()
        elif numbers[0] == '3':
            print(max(stack))
        elif numbers[0] == '4':
            print(min(stack))

stack.reverse()

print(*stack, sep=', ')
