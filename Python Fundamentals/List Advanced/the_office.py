def new_happiness(list_of_ppl_happiness, happiness_factor):
    new_list_of_happiness = [int(x) * happiness_factor for x in list_of_ppl_happiness]

    return new_list_of_happiness


def check_above_average(new_happiness_list):
    happy_above_average = 0
    for happiness in new_happiness_list:
        if happiness >= sum(new_happiness_list) / len(new_happiness_list):
            happy_above_average += 1
    return happy_above_average


list_of_happiness = input().split()
improvement_factor = int(input())
threshold = len(list_of_happiness) / 2

result = check_above_average(new_happiness(list_of_happiness, improvement_factor))

if result < threshold:
    print(f'Score: {result}/{len(list_of_happiness)}. Employees are not happy!')
else:
    print(f"Score: {result}/{len(list_of_happiness)}. Employees are happy!")