number_of_snowballs = int(input())

best_weight = 0
best_time = 0
best_quality = 0
best_value = 0

for current_snowball in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_weight / snowball_time) ** snowball_quality

    if snowball_value > best_value:
        best_value = snowball_value
        best_weight = snowball_weight
        best_time = snowball_time
        best_quality = snowball_quality

print(f"{best_weight} : {best_time} = {int(best_value)} ({best_quality})")