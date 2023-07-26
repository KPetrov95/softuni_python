def mini_calculator(operation, num_one, num_two):
    if operation == "multiply":
        return num_one * num_two
    elif operation == "divide":
        return int(num_one / num_two)
    elif operation == "add":
        return num_one + num_two
    elif operation == "subtract":
        return num_one - num_two


task = input()
first_number = int(input())
second_number = int(input())

print(mini_calculator(task, first_number, second_number))
