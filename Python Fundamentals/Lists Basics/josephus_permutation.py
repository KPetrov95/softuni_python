main_list = input().split()
skip_number_k = int(input())

final_numbers = list()
pos = skip_number_k - 1
index = 0
len_list = (len(main_list))
index = (pos + index) % len_list
#while len_list > 0:
#   index = (pos + index) % len_list
#    final_numbers.append(main_list.pop(index))
#    len_list -= 1

print(index)
print(main_list)
print(final_numbers )