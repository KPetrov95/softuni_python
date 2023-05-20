target_year = int(input())

while True:

    target_year += 1
    str_year = str(target_year)
    set_year = set(map(int, str_year))

    if len(set_year) == len(str_year):
        print(target_year)
        break

