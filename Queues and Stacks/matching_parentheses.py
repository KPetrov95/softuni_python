equation = input()

opening_parenthesis = []

for current_index in range(len(equation)):
    if equation[current_index] == '(':
        opening_parenthesis.append(current_index)
    if equation[current_index] == ')':
        first_parenthesis = opening_parenthesis.pop()
        print(equation[first_parenthesis: current_index + 1])