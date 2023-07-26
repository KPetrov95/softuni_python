list_of_nums = [int(num) for num in input().split(', ')]
current_limiter = 10
while len(list_of_nums) > 0:
    current_list = [num for num in list_of_nums if num <= current_limiter]
    list_of_nums = [num for num in list_of_nums if num not in current_list]
    print(f"Group of {current_limiter}'s: {current_list}")
    current_limiter += 10
