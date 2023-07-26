def sum_numbers(first_num, second_num):
    return first_num + second_num


def subtract(sum_one_and_two, third_num):
    return sum_one_and_two - third_num


def add_and_subtract(num_first, num_second, num_third):
    sum_of_two = num_first + num_second
    return sum_of_two - num_third


num_one = int(input())
num_two = int(input())
num_three = int(input())

print(subtract(sum_numbers(num_one, num_two), num_three))