def find_perfect_number(some_number):
    sum_divisors = 0
    for divisor in range(1, some_number):
        if some_number % divisor == 0:
            sum_divisors += divisor
    if sum_divisors == some_number:
        return True
    return False


number = int(input())

if find_perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")