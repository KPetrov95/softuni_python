num = int(input())

special_nums = [5, 7, 11]

for n in range(1, num + 1):
    numstr = str(n)

    list_of_num = list(map(int, numstr.strip('')))
    sum_nums = sum(list_of_num)
    if sum_nums in special_nums:
        print(f'{n} -> True')
    else:
        print(f'{n} -> False')
