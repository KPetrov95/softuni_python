money_str = input().split(', ')
beggars_count = int(input())
money_int = []
beggars_sum = []
for element in money_str:
    money_int.append(int(element))

start_index = 0

while start_index < beggars_count:
    sum_for_current_beggar = 0
    for money in money_int[start_index::beggars_count]:
        sum_for_current_beggar += money
    beggars_sum.append(sum_for_current_beggar)
    start_index += 1
print(beggars_sum)