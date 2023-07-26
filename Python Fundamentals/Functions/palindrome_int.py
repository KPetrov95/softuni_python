def check_palindrome(some_number):
    if some_number == some_number[::-1]:
        return True
    return False


list_of_strings = input().split(', ')

for number in list_of_strings:
    print(check_palindrome(number))
