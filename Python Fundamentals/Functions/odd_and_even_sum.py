def odd_and_even_sums(single_number_as_string):
    odd_sum = 0
    even_sum = 0
    for char in single_number_as_string:
        num = int(char)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return odd_sum, even_sum


string_of_numbers = input()
result = odd_and_even_sums(string_of_numbers)
print(f"Odd sum = {result[0]}, Even sum = {result[1]}")