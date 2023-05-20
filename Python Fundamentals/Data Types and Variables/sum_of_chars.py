number_of_chars = int(input())
sum_of_chars = 0

for n in range(number_of_chars):
    sum_of_chars += ord(input())

print("The sum equals:", sum_of_chars)