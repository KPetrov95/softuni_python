def first_string_longer(first_string, second_string, sum_of_two):
    for i in range(len(second_string)):
        sum_of_two += ord(first_string[i]) * ord(second_string[i])
    for i in range(len(second_string), len(first_string)):
        sum_of_two += ord(first_string[i])


def second_string_longer(first_string, second_string, sum_of_two):
    for i in range(len(first_string)):
        sum_of_two += ord(first_string[i]) * ord(second_string[i])
    for i in range(len(first_string), len(second_string)):
        sum_of_two += ord(second_string[i])

def equal_strings(first_string, second_string, sum_of_two):
    for i in range(len(first_string)):
        sum_of_two += ord(first_string[i]) * ord(second_string[i])


first, second = input().split()
sum = 0
if len(first) > len(second):
    for i in range(len(second)):
        sum += ord(first[i]) * ord(second[i])
    for i in range(len(second), len(first)):
        sum += ord(first[i])
elif len(first) == len(second):
    for i in range(len(first)):
        sum += ord(first[i]) * ord(second[i])
elif len(first) < len(second):
    for i in range(len(first)):
        sum += ord(first[i]) * ord(second[i])
    for i in range(len(first), len(second)):
        sum += ord(second[i])

print(sum)